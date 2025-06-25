from discord.ext import commands

class Resume(commands.Cog):
  @commands.command(name="resume", aliases=["continuar"])
  async def resume(self, ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
      ctx.voice_client.resume()
      await ctx.send("▶️ Música retomada.")
    else:
      await ctx.send("❌ Nenhuma música pausada no momento.")

async def setup(bot):
  await bot.add_cog(Resume())