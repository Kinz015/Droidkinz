from discord.ext import commands

class Clear(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount: str = "1"):  # Valor padrão é 1
    if amount.lower() == "all":
      await ctx.send("🧹 Limpando **TODAS** as mensagens do canal... Isso pode demorar.", delete_after=3)

      def check(_):
        return True

      deleted = await ctx.channel.purge(limit=None, check=check, bulk=True)
      quantidade = len(deleted)

      texto = "mensagem apagada" if quantidade == 1 else "mensagens apagadas"
      await ctx.send(f"✅ {quantidade} {texto}.", delete_after=5)

    else:
      try:
        amount_int = int(amount)
        # +1 para incluir a mensagem do próprio comando
        deleted = await ctx.channel.purge(limit=amount_int + 1)

        quantidade = len(deleted) - 1  # Desconta o próprio comando

        if quantidade < 0:
          quantidade = 0

        texto = "mensagem apagada" if quantidade == 1 else "mensagens apagadas"
        await ctx.send(f"✅ {quantidade} {texto}.", delete_after=5)

      except ValueError:
        await ctx.send("❌ Use `!clear <quantidade>` ou `!clear all`.", delete_after=5)

async def setup(bot):
  await bot.add_cog(Clear(bot))






