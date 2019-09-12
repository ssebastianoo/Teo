import discord
from discord.ext import commands
import asyncio
import os
import random
import dbl
import logging
import json
import requests

bot = commands.Bot(command_prefix = [')', '<@564064204387123210> '])
bot.remove_command('help')
bot.load_extension("jishaku")



@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('done')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('done')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')
  bot.load_extension(f'cogs.{extension}')
  await ctx.send('done')
  

@bot.event
async def on_ready():
  print('I am', bot.user)

  
  while True:
    
    guilds = len([s for s in bot.guilds]) 
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f'{guilds} servers!'))
    await asyncio.sleep(25)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name='With my master :)'))
    
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name='Wof!'))
    await asyncio.sleep(25)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name='With my master :)'))
    
    await asyncio.sleep(25)
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=')help'))
    await asyncio.sleep(25)
    
  
  


@bot.event
async def on_message(message):
  
  await bot.process_commands(message)
  
  coin = ['Head', 'Tail']
  
  if message.author == bot.user:
    
    if message.content == 'You have launched a coin...':
      
      r = random.choice(coin)
      
      emb = discord.Embed(title=r, colour = 0xfff157)
      
      await asyncio.sleep(0.5)
      await message.edit(embed=emb)
  
@bot.command()
@commands.is_owner()
async def servers(ctx):
  guilds = bot.guilds
  num = len([s for s in bot.guilds])
  result = ""
  for guild in guilds:
    result += f'**{guild.name}**' + f'  `{guild.member_count} members`' + "\n" 
  emb = discord.Embed(title=f'{num} guilds', description=result, colour = 0xfff157)
  await ctx.send(embed=emb)
 
  
@bot.command()
async def ping(ctx):
  """Shows bot latency!"""
  ping = (round(bot.latency * 1000))
  emb = discord.Embed(description = f'{ping}ms', colour = 0xfff157)
  emb.set_author(name = ctx.author.name, url = ctx.author.avatar_url, icon_url = ctx.author.avatar_url)
  await ctx.send(content=None, embed=emb)

@bot.command()
async def help(ctx):

  emb = discord.Embed(title='Help Message', colour = 0xfff157)
  emb.set_thumbnail(url=ctx.author.avatar_url)
  emb.add_field(name='Prefixes', value='`)` `@Teo#8099`', inline=False)
  emb.add_field(name='See bot latency', value='`ping`', inline=False)
  emb.add_field(name='Ban!', value='`ban <user> <reason>`', inline=False)
  emb.add_field(name='Kick!', value='`kick <user> <reason>`', inline=False)
  emb.add_field(name='Purge messages', value='`clear <number of messages>` (max is 100)', inline=False)
  emb.add_field(name='Get user info', value='`about <user>` (if `user` is empty the bot will send message author info)', inline=False)
  emb.add_field(name="See a user's avatar", value='`avatar <user>` (if `user` is empty the bot will send message author info)', inline=False)
  emb.add_field(name='Say something with bot', value='`say "<something>"`', inline = False)
  emb.add_field(name='Get the invite link', value = '`invite`', inline = False)
  emb.add_field(name='Create a channel!', value = '`channel "<name>" "<topic>" "<slowmode>"`', inline=False)
  emb.add_field(name='Flip a coin!', value = '`coinflip`', inline = False)
  emb.add_field(name='Little maths! (+)', value = '`calc <num> <num>`')
  await ctx.send(embed=emb)
  




@bot.command()
async def about(ctx, member: discord.Member=None):

  if not member:

    emb = discord.Embed(title='Name', description = ctx.author.name, colour = 0xfff157)
    emb.set_thumbnail(url=ctx.author.avatar_url)
    emb.add_field(name='Discriminator', value=ctx.author.discriminator)
    emb.add_field(name='Mention', value=f'<@{ctx.author.id}>')
    emb.add_field(name='Status', value=ctx.author.status)
    emb.add_field(name=f'Joined {ctx.author.guild} at', value=ctx.author.joined_at)
    emb.add_field(name='Account Created at', value = ctx.author.created_at)
    emb.add_field(name='Top Role', value=ctx.author.top_role)
    emb.add_field(name='ID', value=ctx.author.id)

    await ctx.send(embed=emb)

    return
    
  if member.bot:
    
    emb = discord.Embed(title='Name', description=member.name, colour = 0xfff157)
    emb.set_thumbnail(url=member.avatar_url)
    emb.add_field(name='Discriminator', value=member.discriminator)
    emb.add_field(name='Mention', value=member.mention)
    emb.add_field(name='Status', value=member.status)
    emb.add_field(name=f'Joined {member.guild} at', value=member.joined_at)
    emb.add_field(name='Account Created at', value = member.created_at)
    emb.add_field(name='Top Role', value=member.top_role)
    emb.add_field(name='ID', value=member.id)
    emb.add_field(name='Bot / User', value='Bot')

    await ctx.send(embed=emb)

    return
 
  

  emb = discord.Embed(title='Name', description=member.name, colour = 0xfff157)
  emb.set_thumbnail(url=member.avatar_url)
  emb.add_field(name='Discriminator', value=member.discriminator)
  emb.add_field(name='Mention', value=member.mention)
  emb.add_field(name='Status', value=member.status)
  emb.add_field(name=f'Joined {member.guild} at', value=member.joined_at)
  emb.add_field(name='Account Created at', value = member.created_at)
  emb.add_field(name='Top Role', value=member.top_role)
  emb.add_field(name='ID', value=member.id)
  emb.add_field(name='Bot / User', value='User')
  
  await ctx.send(embed=emb)
  
@bot.command()
async def guild(ctx):
  
  guild = ctx.guild 
  
  if ctx.author != guild.owner:
    await ctx.message.delete()  
    await ctx.author.send('This command is for server owner only!')
    return
  
  emb = discord.Embed(title='Name', decription=guild.name, colour = 0xfff157)
  emb.set_thumbnail(url=guild.icon_url)
  emb.add_field(name='Owner', value = guild.owner.mention)
  emb.add_field(name='ID', value=guild.id)
  emb.add_field(name=f'{guild.name} has been created at', value = guild.created_at)
  emb.add_field(name='Member Count', value=guild.member_count)

  
  await ctx.send(embed=emb)

@bot.command()
@commands.has_permissions(administrator=True, kick_members=True)
async def clear(ctx, amount=100):
  """Delete some messages"""
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)

@bot.command()
@commands.has_permissions(administrator=True, ban_members=True)
async def ban(ctx, member: discord.Member=None, *, reason):

  if not member:
    
    emb = discord.Embed(title='Nope', descriptipn='**`ban <user> <reason>`**', colour = 0xfffb00)
    await ctx.send(embed=emb)
    return

  if not reason:
    
    emb = discord.Embed(title='Nope', description='**`ban <user> <reason>`**', colour = 0xfffb00)
    await ctx.send(embed=emb)
    return

  emb = discord.Embed(title='Ban!', description = f'{member.mention} has been banned!', colour = 0xcf1313)
  emb.set_thumbnail(url=member.avatar_url)
  emb.add_field(name='Reason', value=reason, inline=False)
  emb.add_field(name='Moderator', value = ctx.author.mention, inline=False)
  
  dm = discord.Embed(title='Banned!', description=f'{member.mention}, you have been banned from {ctx.author.guild}.', colour = 0xcf1313)
  dm.add_field(name='Reason', value=reason, inline=False)
  dm.add_field(name='Moderator', value=ctx.author.mention, inline=False)

  await member.send(embed=dm)
  await member.ban(reason=reason, delete_message_days=1)
  await ctx.send(embed=emb)
  await ctx.message.delete()

@bot.command()
@commands.has_permissions(administrator=True, kick_members=True)
async def kick(ctx, member: discord.Member=None, *, reason):

  if not member:
    
    emb = discord.Embed(title='Nope', descriptipn='**`ban <user> <reason>`**', colour = 0xfffb00)
    await ctx.send(embed=emb)
    return

  if not reason:
    
    emb = discord.Embed(title='Nope', description='**`kick <user> <reason>`**', colour = 0xfffb00)
    await ctx.send(embed=emb)
    return

  emb = discord.Embed(title='Kick!', description = f'{member.mention} has been kicked!', colour = 0xcf1313)
  emb.set_thumbnail(url=member.avatar_url)
  emb.add_field(name='Reason', value=reason, inline=False)
  emb.add_field(name='Moderator', value = ctx.author.mention, inline=False)
  
  dm = discord.Embed(title='Kicked!', description=f'{member.mention}, you have been kicked from {ctx.author.guild}.', colour = 0xcf1313)
  dm.add_field(name='Reason', value=reason, inline=False)
  dm.add_field(name='Moderator', value=ctx.author.mention, inline=False)
  
  await member.send(embed=dm)
  await member.kick(reason=reason)
  await ctx.send(embed=emb)
  await ctx.message.delete()

@bot.command()
@commands.has_permissions(administrator=True, ban_members=True)
async def unban(ctx, *, member):
  
  if ctx.author != 488398758812319745:
    return

  bans = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')
  
  for ban_entry in bans:
    
    user = ban_entry.user
    
    if(user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'{user.mention} unbanned')

@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    emb = discord.Embed(title = 'Error', description = '`ban <member> <reason>`', colour = 0x000000)
    await ctx.send(embed = emb)
    
  if isinstance(error, commands.BadArgument):
    emb = discord.Embed(title='Error', description = 'Member not found.', colour = 0x000000)
    await ctx.send(embed = emb)
    
@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    emb = discord.Embed(title = 'Error', description = '`kick <member> <reason>`', colour = 0x000000)
    await ctx.send(embed = emb)
    
  if isinstance(error, commands.BadArgument):
    emb = discord.Embed(title='Error', description = 'Member not found.', colour = 0x000000)
    await ctx.send(embed = emb)


@bot.command()
async def avatar(ctx, member: discord.Member=None):

  if not member:

    emb = discord.Embed(title=None, description=f"{ctx.author.mention}'s [avatar]({ctx.author.avatar_url})", colour = 0xfff157)  
    emb.set_image(url=ctx.author.avatar_url)

    await ctx.send(embed=emb)

    return

  emb = discord.Embed(title=None, description=f"{member.mention}'s [avatar]({member.avatar_url})", colour = 0xfff157)  
  emb.set_image(url=member.avatar_url)

  await ctx.send(embed=emb)

@bot.command()
async def say(ctx, arg):
  emb = discord.Embed(title=None, description = arg, colour = 0xfff157)
  await ctx.send(embed=emb)
  await ctx.message.delete()

@bot.command()
async def emb(ctx, arg):
  emb = discord.Embed(colour = 0xfff157)
  emb.set_image(url=arg)
  await ctx.send(embed=emb) 
  
@bot.command()
async def invite(ctx):
  
  emb = discord.Embed(title=None, description='You can invite me by clicking [here](https://discordapp.com/api/oauth2/authorize?client_id=564064204387123210&permissions=268789862&scope=bot)', colour = 0xfff157)
  await ctx.send(embed=emb)
  
@bot.command()
@commands.has_permissions(manage_channels=True, administrator = True)
async def channel(ctx, arg1, arg2 , arg3):
  
  await ctx.guild.create_text_channel(name=arg1, topic=arg2, slowmode_delay=arg3)
  
  emb = discord.Embed(title='Name', description = arg1, colour = 0xfff157)
  emb.set_author(icon_url = ctx.author.avatar_url, name=ctx.author.name)
  emb.add_field(name='Topic', value=arg2, inline = False)
  emb.add_field(name='Slowmode', value=f'{arg3} secs', inline = False)
  emb.set_footer(icon_url=ctx.guild.icon_url, text = ctx.guild.name)
  
  await ctx.send(content="I've just created a channel with the following infos:", embed=emb)
  
@channel.error
async def channel_error(ctx, error):
  await ctx.send(error)
  
@bot.command()
async def coinflip(ctx):
  await ctx.send('You have launched a coin...')
  
@bot.command()
async def calc(ctx, arg1, arg2):
  
  res = (int(arg1) + int(arg2))
  
  await ctx.send(f'**`{arg1}` + `{arg2}` = `{res}`**')
  
@bot.event
async def on_guild_join(guild):
  
  channel = bot.get_channel(607358470907494420)
  
  
  emb = discord.Embed(title=f'bot has just joined {guild.name}!', description = f'{guild.member_count} members', colour = 0xfff157)
  emb.set_thumbnail(url=guild.icon_url)
  emb.add_field(name='ID', value = guild.id)
  emb.add_field(name = 'Owner', value = guild.owner)
  
  await channel.send(embed=emb)
  
@bot.event
async def on_guild_remove(guild):
  
  channel = bot.get_channel(607358470907494420)
  
  emb = discord.Embed(title=f'bot has just left {guild.name}!', description = f'{guild.member_count} members', colour = 0xfff157)
  emb.set_thumbnail(url=guild.icon_url)
  emb.add_field(name='ID', value = guild.id)
  
  await channel.send(embed=emb)
  
@bot.command()
async def info(ctx):
  
  emb = discord.Embed(title = 'Developer', description = 'Sebastiano#5005', colour = 0xfff157)
  emb.set_thumbnail(url = bot.user.avatar_url)
  emb.add_field(name = 'GitHub Repo', value = '[Click Me](https://github.com/ssebastianoo/Teo)')
  emb.add_field(name = 'Library', value = '`discord.py`')
  emb.add_field(name = 'Prefixes', value = '`)` and `@Teo#8099`')
  emb.set_image(url = 'https://discordbots.org/api/widget/564064204387123210.png?topcolor=2C2F33&middlecolor=23272A&usernamecolor=FFFFFF&certifiedcolor=FFFFFF&datacolor=FFFFFF&labelcolor=99AAB5&highlightcolor=2C2F33')
  await ctx.send(embed = emb)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')  
  
bot.run('')
