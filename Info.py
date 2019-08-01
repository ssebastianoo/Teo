#Info Commands

#About 

@teo.command()
async def about(ctx, member: discord.Member=None):

  if not member:

    emb = discord.Embed(title='Name', description = ctx.author.name, colour = 0xfff157)
    emb.set_thumbnail(url=ctx.author.avatar_url)
    emb.add_field(name='Discriminator', value=ctx.author.discriminator)
    emb.add_field(name='Mention', value=f'<@{ctx.author.id}>')
    emb.add_field(name='Status', value=ctx.author.status)
    emb.add_field(name=f'Joined{ctx.author.guild} at', value=ctx.author.joined_at)
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
  emb.add_field(name='Top Role', value=member.top_role)
  emb.add_field(name='ID', value=member.id)
  emb.add_field(name='Bot / User', value='User')
  
  await ctx.send(embed=emb)
  
#avatar

@teo.command()
async def avatar(ctx, member: discord.Member=None):

  if not member:

    emb = discord.Embed(title=None, description=f"{ctx.author.mention}'s [avatar]({ctx.author.avatar_url})", colour = 0xfff157)  
    emb.set_image(url=ctx.author.avatar_url)

    await ctx.send(embed=emb)

    return

  emb = discord.Embed(title=None, description=f"{member.mention}'s [avatar]({member.avatar_url})", colour = 0xfff157)  
  emb.set_image(url=member.avatar_url)

  await ctx.send(embed=emb)
