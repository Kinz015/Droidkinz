import discord
from discord.ext import commands

class CommandLogger(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_command(self, ctx):
    channel = self.bot.get_channel(1274819670280507415)  # ID do canal de logs

    embed = discord.Embed(
      title="📄 Comando Executado",
      color=0xFFC222
    )
    embed.set_author(
      name=str(ctx.author),
      icon_url=ctx.author.avatar.url if ctx.author.avatar else None
    )
    embed.add_field(
      name="Canal:",
      value=ctx.channel.mention,
      inline=False
    )
    embed.add_field(
      name="Comando:",
      value=ctx.message.content,
      inline=False
    )

    await channel.send(embed=embed)

async def setup(bot):
  await bot.add_cog(CommandLogger(bot))