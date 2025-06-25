import discord
from discord.ext import commands
import asyncio


class Mute(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  def convert_to_seconds(self, time_str):
    try:
      units = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
      unit = time_str[-1].lower()
      if unit not in units:
        return None
      value = int(time_str[:-1])
      return value * units[unit]
    except:
      return None

  @commands.command(name="mute", aliases=["mutar"])
  @commands.has_guild_permissions(mute_members=True)
  async def mute(self, ctx, member: discord.Member, duration: str = "0"):
    # Verifica se o bot tem permissão de silenciar membros
    if not ctx.guild.me.guild_permissions.mute_members:
      await ctx.send("❌ Eu não tenho permissão para silenciar membros.")
      return
    
    # 🔍 Verificar se existe o cargo "Mutado"
    role = discord.utils.get(ctx.guild.roles, name="🔇 Mutado")
    if not role:
      await ctx.send("❌ Cargo '🔇 Mutado' não encontrado. Crie um cargo chamado **Mutado** e ajuste as permissões nele.")
      return

    # Converte tempo
    seconds = self.convert_to_seconds(duration) if duration != "0" else None
    if duration != "0" and seconds is None:
      await ctx.send("❌ Formato inválido. Use `10s`, `5m`, `2h`, `1d`, `1w`.")
      return

    try:
      # 🔇 Muta na call
      await member.edit(mute=True)
      # 🚫 Adiciona cargo Mutado
      await member.add_roles(role)

      await ctx.send(
        f"🔇 {member.mention} foi mutado na call por **{duration if duration != '0' else 'tempo indefinido'}**."
      )

      if seconds:
        await asyncio.sleep(seconds)
        await member.edit(mute=False)
        await member.remove_roles(role)
        await ctx.send(f"🔊 {member.mention} foi desmutado automaticamente após {duration}.")

    except discord.Forbidden:
      await ctx.send("❌ Não tenho permissão para mutar esse membro.")
    except Exception as e:
      await ctx.send(f"⚠️ Erro ao mutar: `{str(e)}`")

    @commands.command(name="unmute", aliases=["desmutar"])
    @commands.has_guild_permissions(mute_members=True)
    async def unmute(self, ctx, member: discord.Member):
      if not ctx.guild.me.guild_permissions.mute_members:
        await ctx.send("❌ Eu não tenho permissão para desmutar membros.")
        return

      try:
        await member.edit(mute=False)
        await ctx.send(f"🔊 {member.mention} foi desmutado na call.")
      except discord.Forbidden:
        await ctx.send("❌ Não tenho permissão para desmutar esse membro.")
      except Exception as e:
        await ctx.send(f"⚠️ Erro ao desmutar: `{str(e)}`")


async def setup(bot):
    await bot.add_cog(Mute(bot))

