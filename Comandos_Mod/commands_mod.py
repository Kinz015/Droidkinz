class CommandsMod:
  def __init__(self, ctx, client, discord):
    self.ctx = ctx
    self.client = client
    self.discord = discord

  async def mod(self):
    embed = self.discord.Embed(
      title = "Lista de Comandos:",
      description = "- !mod\n- !mute\n- !unmute\n- !clear \n- !ban \n- !kick \n- !timeout \n",
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
