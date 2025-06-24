import discord
from discord.ext import commands
import asyncio
from yt_dlp import YoutubeDL
import os

ytdl_format_options = {
  'format': 'bestaudio/best',
  'quiet': True,
  'default_search': 'ytsearch1',
  'outtmpl': 'downloads/%(title)s.%(ext)s'  # salva os arquivos em /downloads
}

ffmpeg_options = {
  'options': '-vn'
}

ytdl = YoutubeDL(ytdl_format_options)

class Play(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.music_queues = {}  # {guild_id: asyncio.Queue}

  async def ensure_queue(self, ctx):
    guild_id = ctx.guild.id
    if guild_id not in self.music_queues:
      self.music_queues[guild_id] = asyncio.Queue()

  async def play_next(self, ctx):
    guild_id = ctx.guild.id
    queue = self.music_queues[guild_id]

    if queue.empty():
      await ctx.send("🎵 A fila acabou!")
      return

    data = await queue.get()

    title = data['title']
    filename = ytdl.prepare_filename(data)

    source = discord.FFmpegPCMAudio(filename, **ffmpeg_options)

    def after_playing(err):
      if err:
        print(f"Erro ao tocar: {err}")
      # executa o próximo som da fila
      fut = self.play_next(ctx)
      asyncio.run_coroutine_threadsafe(fut, self.bot.loop)

    ctx.voice_client.play(source, after=after_playing)

    await ctx.send(f"▶️ Tocando: **{title}**")

  @commands.command(name="play")
  async def play(self, ctx, *, search: str):
    await self.ensure_queue(ctx)

    # entra no canal de voz
    if not ctx.voice_client:
      if ctx.author.voice:
        await ctx.author.voice.channel.connect()
      else:
        await ctx.send("❌ Você precisa estar em um canal de voz.")
        return

    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, lambda: ytdl.extract_info(search, download=True))

    if 'entries' in data:
      data = data['entries'][0]

    await self.music_queues[ctx.guild.id].put(data)

    await ctx.send(f"✅ Música **{data['title']}** adicionada à fila.")

    # se nada estiver tocando, inicia
    if not ctx.voice_client.is_playing():
      await self.play_next(ctx)

  @commands.command(name="fila")
  async def fila(self, ctx):
    await self.ensure_queue(ctx)
    queue = self.music_queues[ctx.guild.id]._queue
    if not queue:
      await ctx.send("📭 A fila está vazia.")
    else:
      lista = [f"{i+1}. {item['title']}" for i, item in enumerate(queue)]
      await ctx.send("🎶 Fila atual:\n" + "\n".join(lista))

  @commands.command(name="skip")
  async def skip(self, ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
      ctx.voice_client.stop()
      await ctx.send("⏭️ Pulando para a próxima música.")

async def setup(bot):
  await bot.add_cog(Play(bot))