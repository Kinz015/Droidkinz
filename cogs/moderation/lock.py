import discord
from discord.ext import commands

class Lock(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="lock", aliases=["trancar"])
  @commands.has_permissions(manage_channels=True)
  async def lock(self, ctx, canal: discord.TextChannel = None):
    channel = canal or ctx.channel
    await channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(f"🔒 Canal {channel.mention} trancado com sucesso.")

  @commands.command(name="unlock", aliases=["destrancar"])
  @commands.has_permissions(manage_channels=True)
  async def unlock(self, ctx, canal: discord.TextChannel = None):
    channel = canal or ctx.channel
    await channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(f"🔓 Canal {channel.mention} destrancado com sucesso.")

async def setup(bot):
  await bot.add_cog(Lock(bot))
