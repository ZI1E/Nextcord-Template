import nextcord
import json
import os

from pathlib import Path
from nextcord.ext import commands

cwd = Path(__file__).parents[0]
cwd = str(cwd)

def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

settings_file = json.load(open('settings.json'))
bot = commands.Bot(command_prefix=(get_prefix))

@bot.event
async def on_guild_join(guild): # Add default if bot join any guild
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = settings_file['prefix']

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild): # When the bot is left from the guild prefix will deleted automatically
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True) # Change prefix command
async def prefix(ctx, prefix):
    """
    Change Prefix In This Guild Only
    You Can Put Your Custom Prefix
    """
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.reply(f'**Prefix changed to: `{prefix}`**')


if __name__ == "__main__":
    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")
    bot.run(settings_file['token'])