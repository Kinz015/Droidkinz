import discord
from discord.ext import commands

class Queue(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.music_queue = bot.music_queue

    @commands.command(name="fila", aliases=["queue"])
    async def fila(self, ctx):
      queue = self.music_queue.get_queue(ctx.guild.id)

      if not queue or queue.empty():
        embed = discord.Embed(
          title="🎶 Fila de músicas",
          description="📭 A fila está vazia.",
          color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

      items = list(queue._queue)
      limit = 10  # Número máximo de músicas a mostrar

      description = ""
      for i, item in enumerate(items[:limit]):
        title = item.get("title", "Título desconhecido")
        description += f"**{i + 1}.** {title}\n"

      if len(items) > limit:
        description += f"\n...e mais **{len(items) - limit}** músicas na fila."

      embed = discord.Embed(
        title="🎶 Fila de músicas",
        description=description,
        color=discord.Color.green()
      )
      await ctx.send(embed=embed)

async def setup(bot):
  await bot.add_cog(Queue(bot))



