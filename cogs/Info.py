from nextcord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.member) # Cooldown
    async def ping(self, ctx):
        await ctx.reply('Pong !')


def setup(bot):
    bot.add_cog(Info(bot))