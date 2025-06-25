import discord
from discord.ext import commands
import random

class CoinFlip(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="coinflip", aliases=["caraoucoroa", "flip"])
  async def coinflip(self, ctx, escolha: str = None):
    resultado = random.choice(["cara", "coroa"])

    if escolha is None:
      await ctx.send(f"🪙 O resultado foi: **{resultado.capitalize()}**")
      return

    escolha = escolha.lower()
    if escolha not in ["cara", "coroa"]:
      await ctx.send("❓ Escolha inválida! Use `cara` ou `coroa`, ou deixe em branco.")
      return

    if escolha == resultado:
      await ctx.send(f"✅ Deu **{resultado}**! Você acertou, {ctx.author.mention}!")
    else:
      await ctx.send(f"❌ Deu **{resultado}**! Você errou, {ctx.author.mention}!")

async def setup(bot):
  await bot.add_cog(CoinFlip(bot))
