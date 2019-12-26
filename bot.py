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

bot = commands.Bot(command_prefix = commands.when_mentioned_or('))'))
bot.remove_command('help')
bot.load_extension("jishaku")

@bot.command(hidden = True)
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('done')

@bot.command(hidden = True)
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('done')

@bot.command(hidden = True)
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

@bot.command(aliases = ["guilds"], hidden = True)
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
@commands.has_permissions(ban_members = True)
async def idban(ctx, user_id: int, *, reason = None):

  "Ban a member that is not in the actual server"

  try:

      await ctx.guild.ban(discord.Object(id=user_id), reason = reason)
      emb = discord.Embed(title = 'User Banned', description = f'<@{user_id}> has been banned from {ctx.guild.name}!', colour =  0xcf1313, timestamp = ctx.message.created_at)
      emb.add_field(name = 'Moderator', value = ctx.author.mention, inline = False)
      emb.add_field(name = 'Reason', value = reason)
      await ctx.send(embed = emb)

  except AttributeError:

      await ctx.send(f'❌ | {ctx.author.mention} I can\'t find this user, maybe I don\'t share a server with him.')


@bot.command()
async def about(ctx, member: discord.Member=None):

        "see a user info"

        if not member:

            res = ''

            for a in ctx.author.roles:

                if a.name == '@everyone':

                    res += '@everyone '

                else:

                    res += f'{a.mention} '

            emb = discord.Embed(title='Name', description = ctx.author.name, colour = 0xfff157, timestamp = ctx.message.created_at)
            emb.set_thumbnail(url=ctx.author.avatar_url)
            emb.add_field(name='Discriminator', value=ctx.author.discriminator)
            emb.add_field(name='Mention', value=f'<@{ctx.author.id}>')
            emb.add_field(name='Status', value=ctx.author.status)
            if ctx.author.activity:
                emb.add_field(name = 'Activity', value = ctx.author.activity.name)
            emb.add_field(name=f'Joined {ctx.author.guild} at', value=ctx.author.joined_at)
            emb.add_field(name='Account Created at', value = ctx.author.created_at)
            emb.add_field(name='Top Role', value=ctx.author.top_role)
            emb.add_field(name = 'Roles', value = res)
            emb.add_field(name='ID', value=ctx.author.id)

            await ctx.send(embed = emb)

            return

        if member.bot:

            res = ''

            for a in member.roles:

                if a.name == '@everyone':

                    res += '@everyone '

                else:

                    res += f'{a.mention} '

            emb = discord.Embed(title='Name', description=member.name, colour = 0xfff157, timestamp = ctx.message.created_at)
            emb.set_thumbnail(url=member.avatar_url)
            emb.add_field(name='Discriminator', value=member.discriminator)
            emb.add_field(name='Mention', value=member.mention)
            emb.add_field(name='Status', value=member.status)
            if member.activity:
                emb.add_field(name = 'Activity', value = member.activity.name)
            emb.add_field(name=f'Joined {member.guild} at', value=member.joined_at)
            emb.add_field(name='Account Created at', value = member.created_at)
            emb.add_field(name='Top Role', value=member.top_role)
            emb.add_field(name = 'Roles', value = res)
            emb.add_field(name='ID', value=member.id)
            emb.add_field(name='Bot / User', value='Bot')

            await ctx.send(embed=emb)

            return

        res = ''

        for a in member.roles:

                if a.name == '@everyone':

                    res += '@everyone '

                else:

                    res += f'{a.mention} '

        emb = discord.Embed(title='Name', description=member.name, colour = 0xfff157, timestamp = ctx.message.created_at)
        emb.set_thumbnail(url=member.avatar_url)
        emb.add_field(name='Discriminator', value=member.discriminator)
        emb.add_field(name='Mention', value=member.mention)
        emb.add_field(name='Status', value=member.status)
        if member.activity:
            emb.add_field(name = 'Activity', value = member.activity.name)
        emb.add_field(name=f'Joined {member.guild} at', value=member.joined_at)
        emb.add_field(name='Account Created at', value = member.created_at)
        emb.add_field(name='Top Role', value=member.top_role)
        emb.add_field(name = 'Roles', value = res)
        emb.add_field(name='ID', value=member.id)
        emb.add_field(name='Bot / User', value='User')

        await ctx.send(embed=emb)

@bot.command()
async def guild(ctx):

  "See guild info"

  guild = ctx.guild

  res0 = ""
  res1 = ""

  for a in guild.roles:

      if a.name == '@everyone':

          res0 += '@everyone '

      res0 += f'{a.mention} '

  for a in guild.emojis:

      res1 += f'{a} '

  emb = discord.Embed(title='Name', description=guild.name, colour = 0xfff157, timestamp = ctx.message.created_at)
  emb.set_thumbnail(url=guild.icon_url)
  emb.add_field(name='Owner', value = guild.owner.mention, inline = False)
  emb.add_field(name='ID', value=guild.id, inline = False)
  emb.add_field(name=f'{guild.name} has been created at', value = guild.created_at, inline = False)
  emb.add_field(name='Member Count', value=guild.member_count, inline = False)
  emb.add_field(name = "Roles", value = res0, inline = False)
  emb.add_field(name = 'Emojis', value = res1, inline = False)


  await ctx.send(embed=emb)

@bot.command()
async def donate(ctx):

  "Help the bot donating to the developer"

  emb = discord.Embed(title = 'Donate to developer', description = '[Click Me](https://paypal.me/ssebastianoo) Thanks:heart:', colour =  0xfff157)
  await ctx.send(embed = emb)

@bot.command()
@commands.has_permissions(kick_members=True)
async def clear(ctx, amount=100):
  """Delete some messages"""
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None, *, reason=None):

  "Ban a member"

  if not member:

    emb = discord.Embed(title='Nope', descriptipn='**`ban <user> <reason>`**', colour = 0xfffb00)
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
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None, *, reason=None):

  "Kick a member"

  if not member:

    emb = discord.Embed(title='Nope', descriptipn='**`ban <user> <reason>`**', colour = 0xfffb00)
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

  "See a user avatar"

  if not member:

    emb = discord.Embed(title=None, description=f"{ctx.author.mention}'s [avatar]({ctx.author.avatar_url})", colour = 0xfff157, timestamp = ctx.author.joined_at)
    emb.set_image(url=ctx.author.avatar_url)
    emb.set_footer(text = 'Joined At')

    await ctx.send(embed=emb)

    return

  emb = discord.Embed(title=None, description=f"{member.mention}'s [avatar]({member.avatar_url})", colour = 0xfff157, timestamp = member.joined_at)
  emb.set_image(url=member.avatar_url)
  emb.set_footer(text = 'Joined At')

  await ctx.send(embed=emb)

@bot.command()
async def say(ctx, *, message):

  "Say something with Teo"

  if 'http://' or 'https://' in message:

      await ctx.send(f'⛔ | {ctx.author.mention} you put a link, this is not allowed.')

  emb = discord.Embed(description = message, colour = ctx.author.colour)
  await ctx.send(embed=emb)

  await ctx.message.delete()

@bot.command()
async def emb(ctx, link):

  "Embed an image"

  emb = discord.Embed(colour = ctx.author.colour)
  emb.set_image(url=link)
  await ctx.send(embed=emb)

@bot.command()
async def invite(ctx):

  "Bot Invite Link"

  emb = discord.Embed(title=None, description='You can invite me by clicking [here](https://discordapp.com/api/oauth2/authorize?client_id=564064204387123210&permissions=268789862&scope=bot)', colour = 0xfff157)
  await ctx.send(embed=emb)



@bot.command()
@commands.has_permissions(manage_channels=True, administrator = True)
async def channel(ctx, arg1, arg2 , arg3):

  "Create a text channel"

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

  "Flip a coin"

  msg = await ctx.send('You have launched a coin...')

  coin = ['Head', 'Tail']
  r = random.choice(coin)

  emb = discord.Embed(title=r, colour = 0xfff157)

  await asyncio.sleep(0.5)
  await msg.edit(embed=emb)


@bot.command()
async def calc(ctx, arg1, arg2):

  "Make a calc"

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

  "Make a battle"

  author = ctx.author


  if not member:
    await ctx.send('**That is not a valid member.**')
    return


  emb = discord.Embed(description = '*Fighting*', colour = 0xfff157, timestamp = ctx.message.created_at,)
  emb.set_author(name = f'{author.name} vs {member.name}', icon_url = 'https://discordemoji.com/assets/emoji/loading.gif')


  winner = [author.mention, member.mention]

  r = random.choice(winner)

  emb2 = discord.Embed(colour = 0xfff157, timestamp = ctx.message.created_at, description = f'{r} Won!')
  emb2.set_author(name = f'{author.name} vs {member.name}', icon_url = 'https://www.fg-a.com/medieval/2-knight-in-battle.gif')

  battle = await ctx.send(embed = emb)

  await asyncio.sleep(4)

  await battle.edit(embed = emb2)

@bot.command(aliases = ['m'])
@commands.has_permissions(kick_members = True)
async def mute(ctx, member: discord.Member = None, *, reason=None):

  "Mute a member"

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

  "Unmute a member"

  role = discord.utils.get(ctx.guild.roles, name = 'Muted')

  await member.remove_roles(role)

  await ctx.send(f'''**{member.mention} has been unmuted by {ctx.author.mention}**''')





for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')



bot.run('')
