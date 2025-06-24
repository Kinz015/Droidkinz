from discord.ext import commands

class Stop(commands.Cog):
  @commands.command(name="stop")
  async def stop(self, ctx):
    if ctx.voice_client:
      await ctx.voice_client.disconnect()
      await ctx.send("🛑 Bot desconectado.")
    else:
      await ctx.send("❌ O bot não está conectado.")

async def setup(bot):
  await bot.add_cog(Stop())
