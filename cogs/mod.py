import discord
from discord.ext import commands

# colour = 0xfff157

class Moderation(commands.Cog):
    
    def __init__(self, bot):
        
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, id: str = None):

        "Unban a user"
        
        try:
            
            await ctx.guild.unban(discord.Object(id = id))
            emb = discord.Embed(title = 'Unbanned', description = f'<@{id}> has been unbanned from {ctx.guild.name}', colour = discord.Colour.green(), timestamp = ctx.message.created_at)
            emb.add_field(name = 'Moderator', value = ctx.author.mention)
            await ctx.send(embed = emb)

        except AttributeError:

            await ctx.send('❌ | Use `))unban <member id>`')

    

def setup(bot):
  bot.add_cog(Moderation(bot))
