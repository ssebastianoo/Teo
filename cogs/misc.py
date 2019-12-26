import discord
from discord.ext import commands


# colour = 0xfff157

class Misc(commands.Cog):

  def __init__(self, bot):

    self.bot = bot

  @commands.command()
  async def players(self, ctx, *, arg):

    res = ''

    for a in ctx.guild.members:

        if a.activity:

            if a.activity.name == arg:

                res += f'{a} \n'

    emb = discord.Embed(title = f'{arg} players', description = res, colour = 0xfff157, timestamp = ctx.message.created_at)
    await ctx.send(embed = emb)

def setup(bot):
  bot.add_cog(Misc(bot))
