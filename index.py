import discord
import yt_dlp
from discord.ext import commands as commands_import
from dotenv import load_dotenv
import os
from discord.utils import get
from Logs.commands_logs import CommandsLog

FFMPEG_OPTIONS = {'options' : '-vn'}
YDL_OPTIONS = {'format' : 'bestaudio', 'noplaylist' : True}

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')

queue = []

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands_import.Bot('!', case_insensitive = True, intents = intents)

admin = "👻 MOD"

@client.event
async def on_ready():
  print(f'Iniciado')

# Evendo de boas vindas.
@client.event
async def on_member_join(self):
  canalbemvindo = client.get_channel(1211027616845271150)
  role = self.guild.get_role(1211106560869408838)
  await canalbemvindo.send(f"{self.mention} bem vindo ao {self.guild}.")
  await self.add_roles(role)

# COMANDOS YT / MUSICA

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
async def stop(ctx):
  try:
    voice = get(client.voice_clients, guild=ctx.guild)
    await voice.disconnect()
    await ctx.channel.send("O bot foi desconectado.")
  except AttributeError:
    await ctx.channel.send("O bot não esta conectado em nenhum canal de voz.")

@client.command()
async def pause(ctx):
  await ctx.channel.send("Comando em desenvolvimento . . .")
  
@client.command()
async def resume(ctx):
  await ctx.channel.send("Comando em desenvolvimento . . .")

@client.command()
async def flerte(ctx, args):
  user = client.get_user(int(args))
  await ctx.channel.send(f"Oie {user.mention} vem sempre aqui? 😏")
   
@client.command()
async def test(ctx):
  created_at = discord.utils.snowflake_time(393863136979058699)
  print(created_at)

client.run(TOKEN)