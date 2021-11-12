from nextcord.ext import commands
from nextcord.ext.commands import errors


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if isinstance(err, errors.MissingRequiredArgument) or isinstance(err, errors.BadArgument):
            helper = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(
                ctx.command)
            await ctx.send_help(helper)

        elif isinstance(err, errors.CheckFailure):
            pass

        elif isinstance(err, errors.MaxConcurrencyReached):
            await ctx.reply("You've reached max capacity of command usage at once, please finish the previous one...**")

        elif isinstance(err, errors.CommandOnCooldown):
            await ctx.reply(f"**This command is on cooldown... try again in `{err.retry_after:.2f}` seconds.**")

        elif isinstance(err, errors.CommandNotFound):
            await ctx.reply(f"**This command is not found... try again**")


def setup(bot):
    bot.add_cog(Errors(bot))