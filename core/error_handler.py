from discord.ext import commands
import discord

class ErrorHandler(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send("👿 **SE COLOQUE NO SEU LUGAR!** Você não tem permissão pra isso.")
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("⚠️ Você esqueceu de fornecer um argumento obrigatório.")
    elif isinstance(error, commands.BadArgument):
      await ctx.send("❌ Argumento inválido.")
    elif isinstance(error, commands.CommandNotFound):
      return  # Ignora comandos inexistentes
    else:
      await ctx.send("❗ Ocorreu um erro inesperado.")
      raise error  # Para logar no terminal

async def setup(bot):
  await bot.add_cog(ErrorHandler(bot))
