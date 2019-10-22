import discord
from discord.ext import commands 

class Misc(commands.Cog):
  
  def __init__(self, bot):

    self.bot = bot 

  @commands.command()
  async def players(self, ctx, arg):

    num = sum(m.activity == discord.Game(name = arg) for m in ctx.guild.members)
    
    if num == 0:
      
      await ctx.send(f'0 users are playing {arg}')
      return

    res = ''

    for a in ctx.guild.members:

      if a.activity == discord.Game(name = arg):

        res += f'{a} \n'


    await ctx.send(f'''{num} user(s) is/are playing {arg}
>>> {res}''')

def setup(bot):
  bot.add_cog(Misc(bot))  