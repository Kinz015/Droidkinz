class CommandsKick:
  def __init__(self, ctx, member, reason=None):
    self.ctx = ctx
    self.member = member
    self.reason = reason

  async def kick(self):
    mod = self.ctx.message.author
    channel = self.ctx.channel
    msg = f"{self.member.mention} foi expulso por {mod.mention}\nMotivo: {self.reason}" 
    await self.member.kick()
    await channel.send(msg)