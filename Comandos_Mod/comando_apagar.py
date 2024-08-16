class ComandoApagar:
  def __init__(self, ctx, amount):
    self.ctx = ctx
    self.amount = amount

  async def apagar(self):
    if self.amount == "tudo": 
      await self.ctx.channel.purge()
    else: 
      await self.ctx.channel.purge(limit=(int(self.amount) + 1))
