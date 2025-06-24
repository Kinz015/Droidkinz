import discord
from discord.ext import commands

class Mod(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def mod(self, ctx):
    embed = discord.Embed(
      title="📋 Lista de Comandos de Moderação:",
      description=(
        "**!mod** - Exibe esta lista\n"
        "**!mute [usuário]** - Silenciar um membro\n"
        "**!unmute [usuário]** - Dessilenciar um membro\n"
        "**!clear [quantidade]** - Limpar mensagens\n"
        "**!ban [usuário]** - Banir um membro\n"
        "**!kick [usuário]** - Expulsar um membro\n"
        "**!timeout [usuário] [tempo]** - Dar timeout em um membro\n"
      ),
      color=discord.Color.gold()
    )
    embed.set_author(
      name=self.bot.user.name,
      icon_url=self.bot.user.avatar.url
    )
    embed.set_footer(
      text="created by Kinz015",
      icon_url=self.bot.user.avatar.url
    )

    await ctx.send(embed=embed)

async def setup(bot):
  await bot.add_cog(Mod(bot))
