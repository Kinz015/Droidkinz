import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} está online!')

@bot.event
async def setup_hook():
    for folder in ['cogs/moderation', 'cogs/user', 'cogs/music', 'cogs/logs']:
        for filename in os.listdir(folder):
            if filename.endswith('.py') and filename != '__init__.py':
                await bot.load_extension(f"{folder.replace('/', '.')}.{filename[:-3]}")