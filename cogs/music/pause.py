from discord.ext import commands

class Pause(commands.Cog):
  @commands.command(name="pause")
  async def pause(self, ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
      ctx.voice_client.pause()
      await ctx.send("⏸️ Música pausada.")
    else:
      await ctx.send("❌ Nenhuma música tocando para pausar.")

async def setup(bot):
  await bot.add_cog(Pause())
