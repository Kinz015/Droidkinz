import discord
from discord.ext import commands
from music_queue import MusicQueue
from yt_dlp import YoutubeDL
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)

bot.ytdl = YoutubeDL({
    'format': 'bestaudio/best',
    'quiet': True,
    'default_search': 'ytsearch1',
    'outtmpl': 'downloads/%(title)s.%(ext)s'
})


bot.music_queue = MusicQueue()

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} está online!')

@bot.event
async def setup_hook():
    for folder in ['cogs/moderation', 'cogs/user', 'cogs/music', 'cogs/logs']:
        for filename in os.listdir(folder):
            if filename.endswith('.py') and filename != '__init__.py':
                await bot.load_extension(f"{folder.replace('/', '.')}.{filename[:-3]}")
            
    await bot.load_extension("core.error_handler")