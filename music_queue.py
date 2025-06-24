import asyncio

class MusicQueue:
  def __init__(self):
    self.queues = {}

  async def ensure_queue(self, guild_id):
    if guild_id not in self.queues:
      self.queues[guild_id] = asyncio.Queue()
    return self.queues[guild_id]

  def get_queue(self, guild_id):
    return self.queues.get(guild_id)
