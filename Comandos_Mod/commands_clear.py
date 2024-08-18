class CommandsClear:
  def __init__(self, ctx, amount):
    self.ctx = ctx
    self.amount = amount

  async def clear(self):
    if self.amount == "tudo": 
      await self.ctx.channel.purge()
    else: 
      await self.ctx.channel.purge(limit=(int(self.amount) + 1))
