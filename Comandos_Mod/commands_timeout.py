import datetime

class CommandsTimeout:
  def __init__(self, ctx, member, discord, timelimit="0" ):
    self.ctx = ctx
    self.member = member
    self.discord = discord
    self.timelimit = timelimit

  async def timeout(self):
    if "s" in self.timelimit:
      gettime = self.timelimit.strip("s")
      if int(gettime) > 2419000:
        await self.ctx.send("O valor do tempo não pode ser superior a 28 dias")
      else:
        newtime = datetime.timedelta(seconds=int(gettime))
        await self.member.edit(timed_out_until=self.discord.utils.utcnow() + newtime) 
    elif "m" in self.timelimit:
      gettime = self.timelimit.strip("m")
      if int(gettime) > 40320:
        await self.ctx.send("O valor do tempo não pode ser superior a 28 dias")
      else:
        newtime = datetime.timedelta(minutes=int(gettime))
        await self.member.edit(timed_out_until=self.discord.utils.utcnow() + newtime) 
    elif "h" in self.timelimit:
      gettime = self.timelimit.strip("h")
      if int(gettime) > 40320:
        await self.ctx.send("O valor do tempo não pode ser superior a 28 dias")
      else:
        newtime = datetime.timedelta(hours=int(gettime))
        await self.member.edit(timed_out_until=self.discord.utils.utcnow() + newtime) 
    elif "d" in self.timelimit:
      gettime = self.timelimit.strip("d")
      if int(gettime) > 40320:
        await self.ctx.send("O valor do tempo não pode ser superior a 28 dias")
      else:
        newtime = datetime.timedelta(days=int(gettime))
        await self.member.edit(timed_out_until=self.discord.utils.utcnow() + newtime) 
    elif "w" in self.timelimit:
      gettime = self.timelimit.strip("w")
      if int(gettime) > 40320:
        await self.ctx.send("O valor do tempo não pode ser superior a 4 weeks")
      else:
        newtime = datetime.timedelta(weeks=int(gettime))
        await self.member.edit(timed_out_until=self.discord.utils.utcnow() + newtime)
