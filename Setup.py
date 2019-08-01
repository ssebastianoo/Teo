import discord
from discord.ext import commands
import asyncio
import os

teo = commands.Bot(command_prefix = [')', '<@564064204387123210> '])
teo.remove_command('help')

@teo.event
async def on_ready():
  print('I am', teo.user)

  while True:
    await teo.change_presence(status=discord.Status.idle, activity=discord.Game(name='Wof!'))
    await asyncio.sleep(25)
    await teo.change_presence(status=discord.Status.idle, activity=discord.Game(name='With my master :)'))
    await asyncio.sleep(25)
    await teo.change_presence(status=discord.Status.idle, activity=discord.Game(name=')help'))
    await asyncio.sleep(25)
    
teo.run(token)
