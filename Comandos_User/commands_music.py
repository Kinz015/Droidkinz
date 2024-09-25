import discord
from dotenv import load_dotenv
import os

from discord.ext import commands
import yt_dlp
from discord.utils import get

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot('!', case_insensitive = True, intents = intents)

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')
FFMPEG_OPTIONS = {'options' : '-vn'}
YDL_OPTIONS = {'format' : 'bestaudio', 'noplaylist' : True}

queue = []

@client.command()
async def play(ctx, *, search):
  voice_channel = ctx.author.voice.channel if ctx.author.voice else None
  if not voice_channel.connect:
    await ctx.channel.send("Você precisa esta conectado a um canal de voz.")
  if not ctx.voice_client:
    await voice_channel.connect()

  async with ctx.typing():    
    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(f"ytsearch:{search}", download=False)
      if 'entries' in info:
        info = info['entries'][0]
      url = info['url']
      title = info['title']
      queue.append((url, title))
      await ctx.send(f'Adicionado a fila: **{title}**')
    if not ctx.voice_client.is_playing():
      await play_next(ctx)
    
async def play_next(ctx):
  if queue:
    url, title = queue.pop(0)
    source = await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)
    ctx.voice_client.play(source, after=lambda _:client.loop.create_task(play_next(ctx)))
    await ctx.send(f"Now playing **{title}**")
  elif not ctx.voice_client.is_playing():
    await ctx.send("A fila está vazia!")

@client.command()
async def skip(ctx):
  if ctx.voice_client and ctx.voice_client.is_playing():
    ctx.voice_client.stop()
    await ctx.send("Proxima")

@client.command()
async def stop(self):
    try:
      voice = get(self.client.voice_clients, guild=self.ctx.guild)
      await voice.disconnect()
      await self.ctx.channel.send("O bot foi desconectado.")
    except AttributeError:
      await self.ctx.channel.send("O bot não esta conectado em nenhum canal de voz.")
