import discord
from discord.ext import commands
from yt_dlp import YoutubeDL
import os
import asyncio
from music_queue import MusicQueue

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
    self.music_queue = MusicQueue()
    self.current_files = {}  # Armazena o arquivo atual por servidor

  async def play_next(self, ctx):
    queue = self.music_queue.get_queue(ctx.guild.id)
    if queue.empty():
      await ctx.send("📭 A fila acabou.")
      return

    data = await queue.get()
    title = data['title']
    filename = ytdl.prepare_filename(data)

    # Salva o nome do arquivo atual ANTES da música começar
    self.current_files[ctx.guild.id] = filename

    source = discord.FFmpegPCMAudio(filename, **ffmpeg_options)

    def after_playing(err, file_to_remove=filename):
      async def remove_file():
        await asyncio.sleep(1)  # Espera 1 segundo para o FFmpeg liberar o arquivo
        try:
            os.remove(file_to_remove)
            print(f"🗑️ Arquivo removido: {file_to_remove}")
        except Exception as e:
            print(f"⚠️ Erro ao remover {file_to_remove}: {e}")
        fut = self.play_next(ctx)
        asyncio.run_coroutine_threadsafe(fut, self.bot.loop)

      asyncio.run_coroutine_threadsafe(remove_file(), self.bot.loop)

    # Passa a função com lambda para capturar o nome correto do arquivo
    ctx.voice_client.play(source, after=lambda err: after_playing(err))

    await ctx.send(f"▶️ Tocando: **{title}**")

  @commands.command(name="play")
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
