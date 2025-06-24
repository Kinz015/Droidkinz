import discord
from discord.ext import commands

class CommandsList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="comandos")
    async def comandos(self, ctx):
        embed = discord.Embed(
            title="📜 Comandos disponíveis:",
            description=(
                "**!comandos** - Exibe esta lista\n"
                "**!profile [@membro]** - Mostra o perfil de alguém\n"
                "**!play [música/link]** - Toca uma música\n"
                "**!skip** - Pula a música atual\n"
                "**!stop** - Para e limpa a fila\n"
                "**!flerte** - Envia uma cantada aleatória\n"
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
    await bot.add_cog(CommandsList(bot))

