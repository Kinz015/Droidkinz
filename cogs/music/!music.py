import discord
from discord.ext import commands

class NowPlaying(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.music_queue = bot.music_queue

  @commands.command(name="music", aliases=["tocando"])
  async def music(self, ctx):
    play_cog = self.bot.get_cog("Play")

    if not play_cog:
      await ctx.send("⚠️ O módulo de música não está carregado.")
      return

    data = play_cog.current_files.get(ctx.guild.id)

    if data and ctx.voice_client and ctx.voice_client.is_playing():
      title = data.get("title", "Título desconhecido")
      embed = discord.Embed(
          title="🎧 Música tocando agora:",
          description=f"**{title}**",
          color=discord.Color.blue()
      )
      await ctx.send(embed=embed)
    else:
      await ctx.send("📭 Nenhuma música está tocando no momento.")

async def setup(bot):
  await bot.add_cog(NowPlaying(bot))
