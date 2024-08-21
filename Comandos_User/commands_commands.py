class CommandsCommands:
  def __init__(self, ctx, discord, client):
    self.ctx = ctx
    self.discord = discord
    self.client = client

  async def commands(self):
    embed = self.discord.Embed(
    title = "Comandos:",
    description = "- !comandos\n- !profile\n- !play\n- !sair \n- !flerte",
    color = 0xffff00
    )
    embed.set_author(
      name=self.client.user.name, 
      icon_url=self.client.user.avatar.url)
    embed.set_footer(
      text="created by Kinz015",
      icon_url=self.client.user.avatar.url
    )
    await self.ctx.channel.send(embed=embed)
