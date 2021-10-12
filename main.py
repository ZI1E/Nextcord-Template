import json
from nextcord.ext import commands

settings_file = json.load(open('settings.json'))
bot = commands.Bot(command_prefix=settings_file['prefix'])

@bot.command()
async def ping(ctx):
    await ctx.reply('Pong !')

bot.run(settings_file['token'])