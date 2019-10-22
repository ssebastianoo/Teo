import discord
from discord.ext import commands
import asyncio
import os
import random
import dbl
import logging
import json
import requests
import datetime
import time



bot = commands.Bot(command_prefix = commands.when_mentioned_or(')'))
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
  emb.add_field(name = 'Get Infos about the bot', value = '`info`', inline = False)
  emb.add_field(name='See bot latency', value='`ping`', inline=False)
  emb.add_field(name='Ban!', value='`ban <user> <reason>`', inline=False)
  emb.add_field(name = 'Ban with ID!', value = '`idban <user id> <reason>` | I have to share a server with that user.')
  emb.add_field(name='Kick!', value='`kick <user> <reason>`', inline=False)
  emb.add_field(name = 'Mute!', value = '`mute <user> <reason>`')
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
@commands.has_permissions(ban_members = True)
async def idban(ctx, arg: int, *, reason = None):
  
  user = bot.get_user(arg)
  
  await ctx.guild.ban(user, reason = reason, delete_message_days = 3)
  
  emb = discord.Embed(title = 'User Banned', description = f'{user} has been banned from {ctx.guild.name}!', colour =  0xcf1313)
  emb.add_field(name = 'Moderator', value = ctx.author.mention, inline = False)
  emb.add_field(name = 'Reason', value = reason)
  
  await ctx.send(embed = emb)
  await user.send(f'''You have been banned from {ctx.guild.name} by {ctx.author}, with the reason: 
> ```css
{reason}
```''')

@idban.error
async def idban_error(ctx, error):
  
  await ctx.send(f'''**ERROR** ```css
{error}
```''')


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
async def donate(ctx):
  
  emb = discord.Embed(title = 'Donate to developer', description = '[Click Me](paypal.me/ssebastianoo) Thanks:heart:', colour =  0xfff157)

@bot.command()
@commands.has_permissions(administrator=True, kick_members=True)
async def clear(ctx, amount=100):
  """Delete some messages"""
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)

@bot.command()
@commands.has_permissions(administrator=True, ban_members=True)
async def ban(ctx, member: discord.Member=None, *, reason=None):

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

  await member.ban(reason=reason, delete_message_days=1)
  await ctx.send(embed=emb)
  await ctx.message.delete()
  await member.send(embed=dm)
  
  

@bot.command()
@commands.has_permissions(administrator=True, kick_members=True)
async def kick(ctx, member: discord.Member=None, *, reason=None):

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
  
  await member.kick(reason=reason)
  await ctx.send(embed=emb)
  await ctx.message.delete()
  await member.send(embed=dm)

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
    
  
    
  elif isinstance(error, commands.BadArgument):
    emb = discord.Embed(title='Error', description = 'Member not found.', colour = 0x000000)
    await ctx.send(embed = emb)
    
  else:
    emb = discord.Embed(title = 'Error', description = f'> ```{error}```', colour = 0x000000)
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
  msg = await ctx.send('You have launched a coin...')
  
  coin = ['Head', 'Tail']
  r = random.choice(coin)
  
  emb = discord.Embed(title=r, colour = 0xfff157)
  
  await asyncio.sleep(0.5)
  await msg.edit(embed=emb)
      
  
@bot.command()
async def calc(ctx, arg1, arg2):
  
  res = (int(arg1) + int(arg2))
  
  await ctx.send(f'**`{arg1}` + `{arg2}` = `{res}`**')
  
@bot.event
async def on_guild_join(guild):
  
  
  
  channel = bot.get_channel(607358470907494420)
  
  
  emb = discord.Embed(title=f'Teo has just joined {guild.name}!', description = f'{guild.member_count} members', colour = 0xfff157)
  emb.set_thumbnail(url=guild.icon_url)
  emb.add_field(name='ID', value = guild.id)
  emb.add_field(name = 'Owner', value = guild.owner)
  
  await channel.send(embed=emb)
  
@bot.event
async def on_guild_remove(guild):
  

  
  
  channel = bot.get_channel(607358470907494420)
  
  emb = discord.Embed(title=f'Teo has just left {guild.name}!', description = f'{guild.member_count} members', colour = 0xfff157)
  emb.set_thumbnail(url=guild.icon_url)
  emb.add_field(name='ID', value = guild.id)
  
  await channel.send(embed=emb)
  

  

@bot.command()
async def battle(ctx, member: discord.Member=None):
  
  author = ctx.author
  
  
  if not member:
    await ctx.send('**That is not a valid member.**')
    return 
    
  
  emb = discord.Embed(description = '*Fighting*', colour = 0xfff157)
  emb.set_author(name = f'{author.name} vs {member.name}', icon_url = 'https://discordemoji.com/assets/emoji/loading.gif')
  
  
  winner = [author.mention, member.mention]
  
  r = random.choice(winner)
  
  emb2 = discord.Embed(colour = 0xfff157, timestamp = datetime.datetime.now(), description = f'{r} Won!')
  emb2.set_author(name = f'{author.name} vs {member.name}', icon_url = 'https://www.fg-a.com/medieval/2-knight-in-battle.gif')
  emb2.set_footer(text = 'UTC', icon_url = 'https://img.pngio.com/animated-gif-stopwatch-mkkr-design-stopwatch-gif-animation-clock-png-gif-550_550.gif')
  
  battle = await ctx.send(embed = emb)
  
  await asyncio.sleep(4)
  
  await battle.edit(embed = emb2)
  
@bot.command(aliases = ['m'])
@commands.has_permissions(kick_members = True)
async def mute(ctx, member: discord.Member = None, *, reason=None):
  
  role = discord.utils.get(ctx.guild.roles, name = 'Muted')
  
  if role == None:
    
    role = await ctx.guild.create_role(name = 'Muted', reason = 'Bot Muted Role')
    
  await member.add_roles(role)
    
  await ctx.send(f'''**{member.mention} has been muted by {ctx.author.mention}**
*Reason:*
>>> ```css
{reason}```''') 
    
  for channel in ctx.guild.channels:
    
    await channel.set_permissions(role, send_messages = False)
    
@bot.command(alises = ['um'])
@commands.has_permissions(kick_members = True)
async def unmute(ctx, member: discord.Member = None):
  
  role = discord.utils.get(ctx.guild.roles, name = 'Muted')
  
  await member.remove_roles(role)
  
  await ctx.send(f'''**{member.mention} has been unmuted by {ctx.author.mention}**''') 
    
  
    


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')  
        

  
bot.run('NTY0MDY0MjA0Mzg3MTIzMjEw.XXo3qQ.cy-NHLeDZmoPm52EqtLsaegIEsE')
