import os
from discord.ext import commands

class ClearQueue(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.music_queue = bot.music_queue

  @commands.command(name="clearqueue", aliases=["limparfila", "resetfila"])
  async def clearqueue(self, ctx):
    queue = self.music_queue.get_queue(ctx.guild.id)

    if queue and not queue.empty():
      # Pega todos os itens antes de limpar
      items = list(queue._queue)
      queue._queue.clear()

      deletados = 0
      for item in items:
          try:
              filename = self.bot.ytdl.prepare_filename(item)
              if os.path.exists(filename):
                os.remove(filename)
                deletados += 1
          except Exception as e:
            await ctx.send(f"⚠️ Erro ao deletar um arquivo: {e}")

      await ctx.send(f"🗑️ Fila limpa. {deletados} arquivos foram deletados da pasta de downloads.")
    else:
      await ctx.send("📭 A fila já está vazia.")

async def setup(bot):
  await bot.add_cog(ClearQueue(bot))

