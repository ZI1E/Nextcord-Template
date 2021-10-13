import nextcord
import json

from nextcord.ext import commands
from rich.console import Console
from rich.table import Table

console = Console()

settings_file = json.load(open('settings.json'))

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # Our custom print
        table = Table()
        table.add_column("[bold white]Bot info[/bold white]", justify="left", style="bold blue", no_wrap=True)
        table.add_row(f"[bold yellow]Alert:[/bold yellow] Everything Working Well")
        console.print(table)

        await self.bot.change_presence(
            activity=nextcord.Game(name=settings_file['activity']), # Changing bot activity
            status=settings_file['status'] # Bot status // ["idle", "dnd", "online"]
        ) 


def setup(bot):
    bot.add_cog(Events(bot))