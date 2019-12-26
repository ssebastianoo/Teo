import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden = True)
    async def help(self, ctx, command: str = None):

      error = f'```css\nThat command, "{command}", does not exist!\n```'

      res = ''

      emb = discord.Embed(title = f'Help for {ctx.author.name}', colour = 0xfff157)
      emb.set_footer(text = f"Need help about a command? {ctx.prefix.replace(self.bot.user.mention, f'@{self.bot.user.name}#{self.bot.user.discriminator}')}help <command>")


      if command:

        cmd = self.bot.get_command(command)

        if not cmd:

          await ctx.send(error)

          return

        if not cmd.hidden:

          emb.add_field(name = f'{ctx.prefix}{cmd.name} {cmd.signature}', value = cmd.help, inline = False)

          if cmd.aliases:

            emb.add_field(name = 'Aliases', value = cmd.aliases, inline = False)

        else:

          await ctx.send(error)
          return


        await ctx.send(embed = emb)

        return

      for c in self.bot.commands:

        if not c.hidden:

          res += f'**{ctx.prefix}{c.name} {c.signature}**\n*{c.help}*\n\n'

      emb.description = res

      await ctx.send(embed = emb)

def setup(bot):
    bot.add_cog(Help(bot))
