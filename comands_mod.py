class ComandosMod:
  def __init__(self, ctx, amount):
    self.ctx = ctx
    self.amount = amount

  def apagar(self):
    if self.amount == "tudo":
      return self.ctx.channel.purge()
    else: 
      return self.ctx.channel.purge(limit=(int(self.amount) + 1))
    
    
  