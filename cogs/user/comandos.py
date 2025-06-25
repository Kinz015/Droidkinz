import discord
from discord.ext import commands

class CommandsList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="commands", aliases=["comandos"])
    async def commands(self, ctx):
        embed = discord.Embed(
            title="📜 Lista de Comandos",
            description="Aqui estão os comandos disponíveis em inglês e português:",
            color=discord.Color.gold()
        )
        embed.add_field(
            name="👤 Usuário",
            value=(
                "**!profile** / **!perfil [Usuário] (opcional)** — Exibe seu perfil ou o de outro usuário se mencionado\n"
                "**!commands** / **!comandos** — Mostrar a lista de comandos"
            ),
            inline=False
        )
        embed.add_field(
            name="🎵 Música",
            value=(
                "**!play** / **!tocar [Nome ou link do YT]** — Tocar uma música\n"
                "**!pause** / **!pausar** — Pausar a música\n"
                "**!resume** / **!continuar** — Continuar a música\n"
                "**!skip** / **!pular** — Pular para a próxima música\n"
                "**!stop** / **!parar** — Parar a reprodução\n"
                "**!queue** / **!fila** — Ver fila de músicas\n"
                "**!clearqueue** / **!limparfila** — Remove todas as músicas da fila atual\n"
                "**!music** / **!música** — Mostrar status da música atual"
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
    await bot.add_cog(CommandsList(bot))

