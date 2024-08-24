class CommandsProfile:
  def __init__(self, ctx, member, discord, client):
    self.ctx = ctx
    self.member = member
    self.discord = discord
    self.client = client

  async def profile(self):
    roles = ""
    if (not self.member): 
      embed = self.discord.Embed(
      title = f"Perfil de {self.ctx.author.global_name}",
      description = f"Perfil criado desde de ", #colocar data de criação
      color = 0x993399
      )
      embed.set_author(
      name=self.client.user.name, 
      icon_url=self.client.user.avatar.url)
      for role in self.ctx.author.roles:
        if role.name != "@everyone":
          roles = f"- {role.mention}\n" + roles
      embed.add_field(
          name="Tags:",
          value=roles,
          inline= False
      )
      embed.set_image(
        url=self.ctx.author.avatar.url
      )
    else:
      embed = self.discord.Embed(
      title = f"Perfil de {self.member.global_name}",
      description = f"Perfil criado desde de ", #colocar data de criação
      color = 0x993399
      )
      embed.set_author(
      name=self.client.user.name, 
      icon_url=self.client.user.avatar.url)
      for role in self.member.roles:
        if role.name != "@everyone":
          roles = f"- {role.mention}\n" + roles
      embed.add_field(
          name="Tags:",
          value=roles,
          inline= False
      )
      embed.set_image(
        url=self.member.avatar.url
      )
    embed.set_footer(
      text="created by Kinz015",
      icon_url=self.client.user.avatar.url
    )
    await self.ctx.channel.send(embed=embed)