import discord
from discord.ext import commands as commands_import
from dotenv import load_dotenv
import os
from discord.utils import get
from Comandos_User.commands_commands import CommandsCommands
from Comandos_User.commands_profile import CommandsProfile
from Comandos_Mod.commands_mute import CommandsMute
from Comandos_Mod.commands_clear import CommandsClear
from Comandos_Mod.commands_timeout import CommandsTimeout
from Comandos_Mod.commands_mod import CommandsMod
from Comandos_Mod.commands_ban import CommandsBan
from Comandos_Mod.commands_kick import CommandsKick
from Logs.commands_logs import CommandsLog

load_dotenv('.env')
TOKEN = os.getenv('TOKEN')

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

# !comandos
@client.command()
async def commands(ctx, discord=discord, client=client):
  comand = CommandsCommands(ctx, discord, client)
  log = CommandsLog(ctx, ctx.author, client)
  await log.commandsLog()
  await comand.commands()

# !perfil
@client.command()
async def profile(ctx, member:discord.Member=False, discord=discord, client=client):
  comand = CommandsProfile(ctx, member, discord, client)
  log = CommandsLog(ctx, ctx.author, client)
  await log.commandsLog()
  await comand.profile()

# COMANDOS YT / MUSICA



#COMANDOS MOD

# !clear
@client.command()
@commands_import.has_any_role(admin)
async def clear(ctx, amount:str, client=client):
  comand = CommandsClear(ctx, amount)
  log = CommandsLog(ctx, ctx.author, client)
  await log.commandsLog()
  await comand.clear()

# !mute
@client.command()
@commands_import.has_any_role(admin)
async def mute(ctx, member:discord.Member, timelimit, client=client):
  comand = CommandsMute(ctx, member, timelimit)
  log = CommandsLog(ctx, ctx.author, client)
  await log.commandsLog()
  await comand.mute()

# !unmute
@client.command()
@commands_import.has_any_role(admin)
async def unmute(ctx, member:discord.Member, client=client):
  comand = CommandsMute(ctx, member)
  log = CommandsLog(ctx, ctx.author, client)
  await log.commandsLog()
  await comand.unmute()

# !timeout
@client.command()
@commands_import.has_any_role(admin)
async def timeout(ctx, member:discord.Member, timelimit, discord=discord, client=client):
  comand = CommandsTimeout(ctx, member, timelimit, discord)
  log = CommandsLog(ctx, ctx.author, client)
  await log.commandsLog()
  await comand.timeout()

# !mod
@client.command()
@commands_import.has_any_role(admin)
async def mod(ctx, client=client, discord=discord):
  comand = CommandsMod(ctx, client, discord)
  log = CommandsLog(ctx, ctx.author, client)
  await log.commandsLog()
  await comand.mod()
  
# !ban
@client.command()
@commands_import.has_any_role(admin)
async def ban(ctx, member:discord.Member, *, reason=None, client=client):
  comand = CommandsBan(ctx, member, reason)
  log = CommandsLog(ctx, ctx.author, client)
  await log.commandsLog()
  await comand.ban()

# !kick
@client.command()
@commands_import.has_any_role(admin)
async def kick(ctx, member:discord.Member, *, reason=None, client=client):
  comand = CommandsKick(ctx, member, reason)
  log = CommandsLog(ctx, ctx.author, client)
  await log.commandsLog()
  await comand.kick()


client.run(TOKEN)