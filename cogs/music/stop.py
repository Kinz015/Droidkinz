import os
import shutil
from discord.ext import commands

class Stop(commands.Cog):
  @commands.command(name="stop", aliases=["parar"])
  async def stop(self, ctx):
    if ctx.voice_client:
      await ctx.voice_client.disconnect()
      await ctx.send("🛑 Bot desconectado.")

      downloads_path = "downloads"
      if os.path.exists(downloads_path):
        for filename in os.listdir(downloads_path):
          file_path = os.path.join(downloads_path, filename)
          try:
            os.remove(file_path)
          except Exception as e:
            await ctx.send(f"⚠️ Erro ao apagar {filename}: {e}")
    else:
      await ctx.send("❌ O bot não está conectado.")

async def setup(bot):
  await bot.add_cog(Stop())

