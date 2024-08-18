import discord

class CommandsLog:
  def __init__(self, ctx, author, client):
    self.ctx = ctx
    self.author = author
    self.client = client

  async def commandsLog(self):
    channel = self.client.get_channel(1274819670280507415)
    command = f"{self.ctx.message.content}"
    chat = self.ctx.channel.mention
    embed = discord.Embed()
    embed.set_author(
    name=self.ctx.author, 
    icon_url=self.ctx.author.avatar.url)
    embed.add_field(
      name="Comando:",
      value=command,
      inline= False
    )
    embed.add_field(
      name="Chat:",
      value=chat,
      inline= False
    )
    await channel.send(embed=embed)