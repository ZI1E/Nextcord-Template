import nextcord
import json

from nextcord.ext import commands
from rich import table
from rich.console import Console
from rich.table import Table

console = Console()

settings_file = json.load(open('settings.json'))
bot = commands.Bot(command_prefix=settings_file['prefix'])

@bot.command()
async def ping(ctx):
    await ctx.reply('Pong !')

@bot.event
async def on_ready():
    # Our custom print
    table = Table()
    table.add_column("[bold white]Bot info[/bold white]", justify="left", style="bold blue", no_wrap=True)
    table.add_row(f"[bold yellow]Alert:[/bold yellow] Everything Working Well")
    console.print(table)

    await bot.change_presence(
        activity=nextcord.Game(name=settings_file['activity']), # Changing bot activity
        status=settings_file['status'] # Bot status // ["idle", "dnd", "online"]
    ) 

bot.run(settings_file['token'])