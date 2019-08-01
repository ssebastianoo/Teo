#ping

@teo.command()
async def ping(ctx):
  """Shows bot latency!"""
  ping = (teo.latency + 1)
  emb = discord.Embed(title=f'{ctx.author.name} :ping_pong:', description = f'{ping}ms', colour = 0xfff157)
  emb.set_thumbnail(url = ctx.author.avatar_url)
  await ctx.send(content=None, embed=emb)
  
#say

@teo.command()
async def say(ctx, arg):
  emb = discord.Embed(title=None, description = arg, colour = 0xfff157)
  await ctx.send(embed=emb)
  await ctx.message.delete()
  
#emb

@teo.command()
async def emb(ctx, arg):
  emb = discord.Embed(colour = 0xfff157)
  emb.set_image(url=arg)
  await ctx.send(embed=emb)
