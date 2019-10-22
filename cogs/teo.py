import discord
from discord.ext import commands 

class Misc(commands.Cog):
  
  def __init__(self, bot):

    self.bot = bot 

  @commands.command()
  async def info(self, ctx):
      
      emb = discord.Embed(title = "Teo's infos", colour = bot.user.colour)
      emb.add_field(name = 'Bot Guilds', value = len[(u for u in bot.guilds)])
      emb.add_field(name = 'Users', value = len[(s for s in bot.users)])
      emb.add_field(name = 'Support Server', value = '[Click Me](https://discord.gg/w8cbssP)')
      await ctx.send(embed = emb)


def setup(bot):
  bot.add_cog(Misc(bot))  