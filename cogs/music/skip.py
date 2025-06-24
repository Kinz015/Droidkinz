from discord.ext import commands

class Skip(commands.Cog):
  @commands.command(name="skip")
  async def skip(self, ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
      ctx.voice_client.stop()
      await ctx.send("⏭️ Pulando para a próxima música.")
    else:
      await ctx.send("❌ Nenhuma música está tocando no momento.")

async def setup(bot):
  await bot.add_cog(Skip())
