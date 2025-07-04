import discord
from discord.ext import commands

class Kick(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="kick", aliases=["expulsar"])
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} foi expulso. Motivo: {reason or 'Sem motivo.'}")

async def setup(bot):
  await bot.add_cog(Kick(bot))