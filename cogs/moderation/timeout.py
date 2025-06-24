import discord
from discord.ext import commands
import datetime

class Timeout(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  def convert_to_timedelta(self, time_str):
    units = {
      "s": ("seconds", 2419200),  # 28 dias em segundos
      "m": ("minutes", 40320),    # 28 dias em minutos
      "h": ("hours", 672),        # 28 dias em horas
      "d": ("days", 28),          # 28 dias em dias
      "w": ("weeks", 4),          # 4 semanas
    }
    try:
      unit = time_str[-1].lower()
      if unit not in units:
        return None, "Unidade inválida. Use s,m,h,d,w."
      value = int(time_str[:-1])
      name, max_value = units[unit]
      if value > max_value:
        return None, f"Valor máximo para {unit} é {max_value}."
      return datetime.timedelta(**{name: value}), None
    except Exception:
      return None, "Formato inválido. Use, por exemplo: 10s, 5m, 2h, 1d, 1w."

  @commands.command()
  @commands.has_permissions(moderate_members=True)  # permissão necessária para timeout no Discord
  async def timeout(self, ctx, member: discord.Member, duration: str = None):
    """Aplica timeout no membro por um período definido"""
    if not ctx.guild.me.guild_permissions.moderate_members:
      await ctx.send("❌ Eu não tenho permissão para aplicar timeout.")
      return

    if duration is None:
      await ctx.send("❌ Você deve especificar a duração do timeout, ex: `10m`, `1h`.")
      return

    delta, error = self.convert_to_timedelta(duration)
    if error:
      await ctx.send(f"❌ {error}")
      return

    until = discord.utils.utcnow() + delta

    try:
      await member.edit(timed_out_until=until)
      await ctx.send(f"⏱️ {member.mention} foi colocado em timeout por {duration}.")
    except discord.Forbidden:
      await ctx.send("❌ Não tenho permissão para modificar esse membro.")
    except Exception as e:
      await ctx.send(f"⚠️ Erro ao aplicar timeout: {e}")

  @commands.command()
  @commands.has_permissions(moderate_members=True)
  async def removetimeout(self, ctx, member: discord.Member):
    """Remove timeout do membro"""
    if not ctx.guild.me.guild_permissions.moderate_members:
      await ctx.send("❌ Eu não tenho permissão para remover timeout.")
      return

    try:
      await member.edit(timed_out_until=None)
      await ctx.send(f"✅ Timeout removido de {member.mention}.")
    except discord.Forbidden:
      await ctx.send("❌ Não tenho permissão para modificar esse membro.")
    except Exception as e:
      await ctx.send(f"⚠️ Erro ao remover timeout: {e}")

async def setup(bot):
  await bot.add_cog(Timeout(bot))
