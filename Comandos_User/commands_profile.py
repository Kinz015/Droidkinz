class CommandsProfile:
  def __init__(self, ctx, member, discord):
    self.ctx = ctx
    self.member = member
    self.discord = discord

  async def profile(self):
    created_at = self.discord.utils.snowflake_time(393863136979058699)
    embed = self.discord.Embed(
      title = f"Perfil de {self.ctx.author.global_name}",
      description = f"Perfil criado desde {created_at} de ",
      color = 0x993399
    )
    roles = ""
    for role in self.ctx.author.roles:
      if role.name != "@everyone":
        roles = f"- {role.mention}\n" + roles
    embed.add_field(
        name="Tags:",
        value=roles,
        inline= False
      )
    embed.set_author(
      name=self.client.user.name, 
      icon_url=self.client.user.avatar.url)
    embed.set_image(
      url=self.ctx.author.avatar.url
    )
    embed.set_footer(
      text="created by Kinz015",
      icon_url=self.client.user.avatar.url
    )
    await self.ctx.channel.send(embed=embed)