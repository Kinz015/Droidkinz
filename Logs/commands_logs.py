import discord

class CommandsLog:
  def __init__(self, ctx, author, client):
    self.ctx = ctx
    self.author = author
    self.client = client

  async def commandsLog(self):
    channel = self.client.get_channel(1274819670280507415)
    msg = f"Comando: {self.ctx.message.content}"
    embed = discord.Embed(
    title = f"",
    description = msg,
    color = 0xFFC222
    )
    embed.set_author(
    name=self.ctx.author, 
    icon_url=self.ctx.author.avatar.url)
    await channel.send(embed=embed)