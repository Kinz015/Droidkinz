import discord
from discord.ext import commands

class Ban(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="ban", aliases=["banir"])
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} foi banido. Motivo: {reason if reason else 'Sem motivo.'}")

async def setup(bot):
  await bot.add_cog(Ban(bot))