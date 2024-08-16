import asyncio

class ComandosMute:
  def __init__(self, ctx, member, timelimit="0"):
    self.ctx = ctx
    self.member = member
    self.timelimit = timelimit
    
  async def mutar(self):
    role_muted = self.ctx.guild.get_role(1253179790702411836)
    time_muted = 0
    if "s" in self.timelimit:
      gettime = int(self.timelimit.strip("s"))
      if gettime > 2419000:
        self.ctx.send("O valor do tempo não pode ser superior a 28 dias")
      else:
        time_muted += gettime
    elif "m" in self.timelimit:
      gettime = int(self.timelimit.strip("m"))
      if gettime > 40320:
        self.ctx.send("O valor do tempo não pode ser superior a 28 dias")
      else:
        gettime *= 60
        time_muted += gettime
    elif "h" in self.timelimit:
      gettime = int(self.timelimit.strip("h"))
      if int(gettime) > 40320:
        self.ctx.send("O valor do tempo não pode ser superior a 28 dias")
      else:
        gettime *= 3600
        time_muted += gettime
    elif "d" in self.timelimit:
      gettime = int(self.timelimit.strip("d"))
      if gettime > 672:
        self.ctx.send("O valor do tempo não pode ser superior a 28 dias")
      else:
        gettime *= 86400
        time_muted += gettime
    elif "w" in self.timelimit:
      gettime = int(self.timelimit.strip("w"))
      if gettime > 4:
        self.ctx.send("O valor do tempo não pode ser superior a 4 semanas")
      else:
        gettime *= 604800
        time_muted += gettime
    await self.member.edit(mute=True)
    await self.member.add_roles(role_muted)
    await asyncio.sleep(int(time_muted))
    await self.member.edit(mute=None)
    await self.member.remove_roles(role_muted)
    
  async def desmutar(self):
    role_muted = self.ctx.guild.get_role(1253179790702411836)
    await self.member.edit(mute=None)
    await self.member.remove_roles(role_muted)
  