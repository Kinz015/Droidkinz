import discord
from discord.ext import commands
from yt_dlp import YoutubeDL
import os
import asyncio

ytdl = YoutubeDL({
  'format': 'bestaudio/best',
  'quiet': True,
  'default_search': 'ytsearch1',
  'outtmpl': 'downloads/%(title)s.%(ext)s'
})

ffmpeg_options = {
  'options': '-vn'
}

class Play(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.music_queue = bot.music_queue
    self.current_files = {}  # Armazena o arquivo atual por servidor

  async def play_next(self, ctx):
    queue = self.music_queue.get_queue(ctx.guild.id)

    if queue.empty():
      # Só envia mensagem se o bot ainda estiver conectado
      if ctx.voice_client and ctx.voice_client.is_connected():
        await ctx.send("📭 A fila acabou. O bot vai se desconectar em 5 minutos se nenhuma música for adicionada.")

        await asyncio.sleep(300)  # 5 minutos
        queue = self.music_queue.get_queue(ctx.guild.id)

        # Verifica de novo se ainda está vazio E se o bot continua conectado
        if queue.empty() and ctx.voice_client and ctx.voice_client.is_connected():
          await ctx.voice_client.disconnect()
          await ctx.send("🛑 Bot desconectado por inatividade.")
        return

    data = await queue.get()
    title = data['title']
    filename = self.bot.ytdl.prepare_filename(data)

    self.current_files[ctx.guild.id] = {
      "filename": filename,
      "title": title
    }

    source = discord.FFmpegPCMAudio(filename, **ffmpeg_options)

    def after_playing(err):
        try:
          os.remove(filename)
        except Exception:
          pass
        fut = self.play_next(ctx)
        asyncio.run_coroutine_threadsafe(fut, self.bot.loop)

    ctx.voice_client.play(source, after=after_playing)
    await ctx.send(f"▶️ Tocando: **{title}**")

  @commands.command(name="play", aliases=["tocar"])
  async def play(self, ctx, *, search: str):
    queue = await self.music_queue.ensure_queue(ctx.guild.id)

    voice_channel = ctx.author.voice.channel if ctx.author.voice else None
    if not voice_channel:
      await ctx.send("❌ Você precisa estar em um canal de voz.")
      return

    if not ctx.voice_client:
      vc = await voice_channel.connect()
    else:
      vc = ctx.voice_client

    # Baixar a música
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, lambda: ytdl.extract_info(search, download=True))
    if 'entries' in data:
      data = data['entries'][0]

    await queue.put(data)
    await ctx.send(f"✅ Música **{data['title']}** adicionada à fila.")

    if not vc.is_playing():
      await self.play_next(ctx)

async def setup(bot):
  await bot.add_cog(Play(bot))
