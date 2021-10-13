from nextcord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ping(ctx):
        await ctx.reply('Pong !')


def setup(bot):
    bot.add_cog(Info(bot))