import discord
from discord.ext import commands

class Profile(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="profile", aliases=["perfil"])
  async def profile(self, ctx, member: discord.Member = None):
    if member is None:
      member = ctx.author

    roles = ""
    for role in member.roles:
      if role.name != "@everyone":
        roles = f"- {role.mention}\n" + roles

    embed = discord.Embed(
      title=f"Perfil de {member.display_name}",
      description=(
        f"📅 Conta criada em: {member.created_at.strftime('%d/%m/%Y')}\n"
        f"👥 Entrou no servidor em: {member.joined_at.strftime('%d/%m/%Y') if member.joined_at else 'Data desconhecida'}"
      ),
      color=0x993399
    )

    embed.set_author(
      name=self.bot.user.name,
      icon_url=self.bot.user.avatar.url
    )

    if roles:
      embed.add_field(
        name="Tags:",
        value=roles,
        inline=False
      )

    embed.set_image(
      url=member.avatar.url if member.avatar else member.default_avatar.url
    )

    embed.set_footer(
      text="created by Kinz015",
      icon_url=self.bot.user.avatar.url
    )

    await ctx.send(embed=embed)

async def setup(bot):
  await bot.add_cog(Profile(bot))
