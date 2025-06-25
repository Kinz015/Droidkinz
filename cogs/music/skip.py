from discord.ext import commands
import asyncio
import os

class Skip(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="skip")
  async def skip(self, ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
      # Tenta deletar o arquivo atual antes de pular
      play_cog = self.bot.get_cog("Play")
      if play_cog:
        filename = play_cog.current_files.get(ctx.guild.id)
        if filename and os.path.exists(filename):
          try:
            os.remove(filename)
            print(f"Arquivo {filename} removido com sucesso.")
          except Exception as e:
            print(f"Erro ao remover {filename}: {e}")

      ctx.voice_client.stop()
      await ctx.send("⏭️ Pulando para a próxima música.")

      # Garante que continue tocando
      await asyncio.sleep(1)
      if not ctx.voice_client.is_playing():
        if play_cog:
          await play_cog.play_next(ctx)
    else:
      await ctx.send("❌ Nenhuma música está tocando no momento.")

async def setup(bot):
  await bot.add_cog(Skip(bot))
