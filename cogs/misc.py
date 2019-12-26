import discord
from discord.ext import commands
import json
import requests

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

  @commands.command()
  async def dog(self, ctx):

    "Get a random dog's image"

    dogapi = requests.get('https://dog.ceo/api/breeds/image/random').json()

    emb = discord.Embed(title = 'Doggo', url = dogapi['message'], colour = 0xfff157)
    emb.set_image(url = dogapi['message'])
    emb.set_footer(text = 'API: https://dog.ceo/api/breeds/image/random')

    await ctx.send(embed = emb)

  @commands.command()
  async def emoji(self, ctx, emoji: discord.Emoji = None):

    "see an emoji's info"

    i = False

    emb = discord.Embed(title = emoji.name, description = emoji, colour = 0xfff157)
    emb.add_field(name = 'ID', value = emoji.id, inline = i)
    emb.add_field(name = 'Created At', value = emoji.created_at, inline = i)
    emb.add_field(name = 'Raw', value = f'`<:{emoji.name}:{emoji.id}>`', inline = i)
    if emoji.animated:
      emb.add_field(name = 'Animated', value = 'True')
    else: 
      emb.add_field(name = 'Animated', value = 'False')
    emb.set_image(url = emoji.url)



def setup(bot):
  bot.add_cog(Misc(bot))
