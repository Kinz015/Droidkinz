import discord
from discord.ext import commands

class MemberLog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.member_log_channel_id = 1405636860201664683 # ID do canal de log de membros

  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = self.bot.get_channel(self.member_log_channel_id)
    if not channel:
      return

    embed = discord.Embed(
      title="✅ Membro Entrou",
      color=0x00FF00
    )
    embed.set_author(
      name=str(member),
      icon_url=member.avatar.url if member.avatar else None
    )
    embed.add_field(
      name="Membro:",
      value=member.mention,  # menciona o usuário
      inline=False
    )
    embed.add_field(
      name="ID:",
      value=member.id,
      inline=False
    )
    embed.add_field(
      name="Conta criada em:",
      value=discord.utils.format_dt(member.created_at, style="R"),
      inline=False
    )

    await channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_member_remove(self, member):
    channel = self.bot.get_channel(self.member_log_channel_id)
    if not channel:
      return

    embed = discord.Embed(
      title="👋 Membro Saiu",
      color=0xFF5555
    )
    embed.set_author(
      name=str(member),
      icon_url=member.avatar.url if member.avatar else None
    )
    embed.add_field(
      name="Membro:",
      value=member.mention,  # menciona o usuário
      inline=False
    )
    embed.add_field(
      name="ID:",
      value=member.id,
      inline=False
    )

    await channel.send(embed=embed)

async def setup(bot):
  await bot.add_cog(MemberLog(bot))
