import discord
from discord.ext import commands

class MessageLogger(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message_delete(self, message):
    if message.author.bot:
      return

    channel = self.bot.get_channel(1405629837556842586)  # ID do canal de logs

    embed = discord.Embed(
      title="🗑️ Mensagem Apagada",
      color=0xFF5555
    )
    embed.set_author(
      name=str(message.author),
      icon_url=message.author.avatar.url if message.author.avatar else None
    )
    embed.add_field(
      name="Canal:",
      value=message.channel.mention,
      inline=False
    )
    embed.add_field(
      name="Conteúdo:",
      value=message.content or "*[Sem texto - possivelmente só mídia]*",
      inline=False
    )

    await channel.send(embed=embed)

  # Mensagens editadas
  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
    if before.author.bot:
      return

    if before.content == after.content:
      return  # Ignora edições sem alteração real

    channel = self.bot.get_channel(1405629837556842586)  # ID do canal de logs

    embed = discord.Embed(
      title="✏️ Mensagem Editada",
      color=0xFFC222
    )
    embed.set_author(
      name=str(before.author),
      icon_url=before.author.avatar.url if before.author.avatar else None
    )
    embed.add_field(
      name="Canal:",
      value=before.channel.mention,
      inline=False
    )
    embed.add_field(
      name="Antes:",
      value=before.content or "*[Sem texto]*",
      inline=False
    )
    embed.add_field(
      name="Depois:",
      value=after.content or "*[Sem texto]*",
      inline=False
    )

    await channel.send(embed=embed)

async def setup(bot):
  await bot.add_cog(MessageLogger(bot))