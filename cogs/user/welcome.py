from discord.ext import commands
import discord

class Welcome(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
    canal_bemvindo = self.bot.get_channel(1211027616845271150)
    role = member.guild.get_role(1211106560869408838)

    if canal_bemvindo:
      await canal_bemvindo.send(f"{member.mention} bem-vindo ao {member.guild.name}!")

    if role:
      await member.add_roles(role)

async def setup(bot):
  await bot.add_cog(Welcome(bot))
