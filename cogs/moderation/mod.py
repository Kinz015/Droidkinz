import discord
from discord.ext import commands

class Mod(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="mod", aliases=["moderação"])
  @commands.has_permissions(kick_members=True)
  async def mod(self, ctx):
    embed = discord.Embed(
      title="📜 Lista de Comandos",
      description="Aqui estão os comandos disponíveis em inglês e português:",
      color=discord.Color.gold()
    )
    embed.add_field(
      name="🛡️ Moderação",
      value=(
        "**!ban** / **!banir [usuário]** — Banir um usuário\n"
        "**!kick** / **!expulsar [usuário]** — Expulsar um usuário\n"
        "**!mute** / **!mutar [usuário]** — Mutar um usuário\n"
        "**!unmute** / **!desmutar [usuário]** — Dessilenciar um membro\n"
        "**!timeout** / **!castigo [usuário]** — Dar timeout a um usuário\n"
        "**!removetimeout** / **!removercastigo [usuário]** — Remover timeout a um usuário\n"
        "**!clear** / **!limpar [quantidade]** — Limpar mensagens\n"
        "**!lock** / **!trancar** — Tranca o canal de texto"
        "**!unlock** / **!destrancar** — Destranca o canal de texto"
        "**!mod** / **!moderação** — Mostrar a lista de comandos de moderação"
      ),
      inline=False
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
