import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from discord.utils import get
import datetime
import asyncio
from Comandos_Mod.comands_mute import ComandosMute
from Comandos_Mod.comando_apagar import ComandoApagar

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot('!', case_insensitive = True, intents = intents)

admin = "👻 MOD"

@client.event
async def on_ready():
  print(f'Iniciado')

# Evendo de boas vindas.
@client.event
async def on_member_join(self):
  canalbemvindo = client.get_channel(1211027616845271150)
# Pegando o cargo
  role = self.guild.get_role(1211106560869408838)
  mensagem = await canalbemvindo.send(f"{self.mention} bem vindo ao {self.guild}.")
  await self.add_roles(role)

# !comandos
@client.command()
async def comandos(ctx):
# Criar uma embed
  embed = discord.Embed(
    title = "Lista de Comandos:",
    description = "- !comandos\n- !perfil\n- !play\n- !sair \n- !flerte",
    color = 0xffff00
  )
  embed.set_author(
    name=client.user.name, 
    icon_url=client.user.avatar.url)
  embed.set_footer(
    text="created by Kinz015",
    icon_url=client.user.avatar.url
  )
  mensagem = await ctx.channel.send(embed=embed)
  await asyncio.sleep(10)
  await ctx.message.delete()
  await mensagem.delete()

# !perfil
@client.command()
async def perfil(ctx):
  created_at = discord.utils.snowflake_time(393863136979058699)
  embed = discord.Embed(
    title = f"Perfil de {ctx.author.global_name}",
    description = f"Perfil criado desde {created_at} de ",
    color = 0x993399
  )
  roles = ""
  for role in ctx.author.roles:
    if role.name != "@everyone":
      roles = f"- {role.mention}\n" + roles
  embed.add_field(
      name="Tags:",
      value=roles,
      inline= False
    )
  embed.set_author(
    name=client.user.name, 
    icon_url=client.user.avatar.url)
  embed.set_image(
    url=ctx.author.avatar.url
  )
  embed.set_footer(
    text="created by Kinz015",
    icon_url=client.user.avatar.url
  )
  await ctx.channel.send(embed=embed)

# COMANDOS YT / MUSICA
@client.command()
async def join(ctx, args):
  try:
    call = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
      await voice.move_to(call)
    else:
      voice = await call.connect()
      await discord.send_audio_packet(args, encode=True)
  except AttributeError:
    await ctx.channel.send("Você precisa esta conectado a um canal de voz.")

@client.command()
async def play(ctx, args):
  try:
    call = ctx.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
      await voice.move_to(call)
    else:
      voice = await call.connect()
      await discord.send_audio_packet(args, encode=True)
  except AttributeError:
    await ctx.channel.send("Você precisa esta conectado a um canal de voz.")

@client.command()
async def pause(ctx):
  await ctx.channel.send("Comando em desenvolvimento . . .")
  

@client.command()
async def resume(ctx):
  await ctx.channel.send("Comando em desenvolvimento . . .")

@client.command()
async def stop(ctx):
  await ctx.channel.send("Comando em desenvolvimento . . .")

@client.command()
async def sair(ctx):
  try:
    voice = get(client.voice_clients, guild=ctx.guild)
    await voice.disconnect()
  except AttributeError:
    await ctx.channel.send("O bot não esta conectado em nenhum canal de voz.")

@client.command()
async def flerte(ctx, args):
  user = client.get_user(int(args))
  await ctx.channel.send(f"Oie {user.mention} vem sempre aqui? 😏")
   
@client.command()
async def test(ctx):
  created_at = discord.utils.snowflake_time(393863136979058699)
  print(created_at)

#COMANDOS MOD

@client.command()
@commands.has_any_role(admin)
async def apagar(ctx, amount:str):
  comand = ComandoApagar(ctx, amount)
  await comand.apagar()

@client.command()
@commands.has_any_role(admin)
async def mutar(ctx, member:discord.Member, timelimit):
  comand = ComandosMute(ctx, member, timelimit)
  await comand.mutar()

@client.command()
@commands.has_any_role(admin)
async def desmutar(ctx, member:discord.Member):
  comand = ComandosMute(ctx, member)
  await comand.mutar()

@client.command()
@commands.has_any_role(admin)
async def mod(ctx):
  embed = discord.Embed(
    title = "Lista de Comandos:",
    description = "- !apagar",
    color = 0xffff00
  )
  embed.set_author(
    name=client.user.name, 
    icon_url=client.user.avatar.url)
  embed.set_footer(
    text="created by Kinz015",
    icon_url=client.user.avatar.url
  )
  mensagem = await ctx.channel.send(embed=embed)

@client.command()
@commands.has_any_role(admin)
async def ban(ctx, member:discord.Member, *, reason=None):
  mod = ctx.message.author
  channel = ctx.channel
  msg = f"{member.mention} foi banido por {mod.mention}\nMotivo: {reason}" 
  await member.ban()
  await channel.send(msg)

@client.command()
@commands.has_any_role(admin)
async def kick(ctx, member:discord.Member, *, reason=None):
  mod = ctx.message.author
  channel = ctx.channel
  msg = f"{member.mention} foi expulso por {mod.mention}\nMotivo: {reason}" 
  await member.kick()
  await channel.send(msg)

@client.command()
@commands.has_any_role(admin)
async def timeout(ctx, member:discord.Member, timelimit):
  if "s" in timelimit:
    gettime = timelimit.strip("s")
    if int(gettime) > 2419000:
      await ctx.send("O valor do tempo não pode ser superior a 28 dias")
    else:
      newtime = datetime.timedelta(seconds=int(gettime))
      await member.edit(timed_out_until=discord.utils.utcnow() + newtime) 
  elif "m" in timelimit:
    gettime = timelimit.strip("m")
    if int(gettime) > 40320:
      await ctx.send("O valor do tempo não pode ser superior a 28 dias")
    else:
      newtime = datetime.timedelta(minutes=int(gettime))
      await member.edit(timed_out_until=discord.utils.utcnow() + newtime) 
  elif "h" in timelimit:
    gettime = timelimit.strip("h")
    if int(gettime) > 40320:
      await ctx.send("O valor do tempo não pode ser superior a 28 dias")
    else:
      newtime = datetime.timedelta(hours=int(gettime))
      await member.edit(timed_out_until=discord.utils.utcnow() + newtime) 
  elif "d" in timelimit:
    gettime = timelimit.strip("d")
    if int(gettime) > 40320:
      await ctx.send("O valor do tempo não pode ser superior a 28 dias")
    else:
      newtime = datetime.timedelta(days=int(gettime))
      await member.edit(timed_out_until=discord.utils.utcnow() + newtime) 
  elif "w" in timelimit:
    gettime = timelimit.strip("w")
    if int(gettime) > 40320:
      await ctx.send("O valor do tempo não pode ser superior a 4 weeks")
    else:
      newtime = datetime.timedelta(weeks=int(gettime))
      await member.edit(timed_out_until=discord.utils.utcnow() + newtime) 

  
client.run(TOKEN)