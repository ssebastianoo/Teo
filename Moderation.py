#List of moderation command!

#ban 

@teo.command()
@commands.has_permissions(administrator=True, ban_members=True)
async def ban(ctx, member: discord.Member=None, *, reason):

  if not member:
    
    emb = discord.Embed(title='Nope', descriptipn='**`ban <user> <reason>`**', colour = 0xfffb00)
    await ctx.send(embed=emb)
    return

  if reason == None:
    
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
  await member.send(embed=dm)
  await ctx.message.delete()
  
#kick
 
@teo.command()
@commands.has_permissions(administrator=True, kick_members=True)
async def kick(ctx, member: discord.Member=None, *, reason):

  if not member:
    
    emb = discord.Embed(title='Nope', descriptipn='**`ban <user> <reason>`**', colour = 0xfffb00)
    await ctx.send(embed=emb)
    return

  if reason == None:
    
    emb = discord.Embed(title='Nope', descriptipn='**`kick <user> <reason>`**', colour = 0xfffb00)
    await ctx.send(embed=emb)
    return

  emb = discord.Embed(title='Kick!', description = f'{member.mention} has been kicked!', colour = 0xcf1313)
  emb.set_thumbnail(url=member.avatar_url)
  emb.add_field(name='Reason', value=reason, inline=False)
  emb.add_field(name='Moderator', value = ctx.author.mention, inline=False)
  
  dm = discord.Embed(title='Kickef!', description=f'{member.mention}, you have been kicked from {ctx.author.guild}.', colour = 0xcf1313)
  dm.add_field(name='Reason', value=reason, inline=False)
  dm.add_field(name='Moderator', value=ctx.author.mention, inline=False)
  
  await member.kick(reason=reason)
  await member.send(embed=dm)
  await ctx.send(embed=emb)
  await ctx.message.delete()
  
#unban
  
@teo.command()
@commands.has_permissions(administrator=True, ban_members=True)
async def unban(ctx, *, member):

  bans = await ctx.guild.bans()
  
  for ban_entry in bans:

    user = ban_entry.user
    
    await ctx.guild.unban(user)
      
    emb = discord.Embed(title='Unbanned!', description=f'{user.mention} has been unbanned!', colour = 0xfff157)
    await ctx.send(embed=emb)
    return
 
#clear 

@teo.command()
@commands.has_permissions(administrator=True. kick_members=True)
async def clear(ctx, amount=100):
  """Delete some messages"""
  await ctx.channel.purge(limit=amount)
  
