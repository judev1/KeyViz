from discord.ext import commands
from discord import Status, Game
import sys

sys.path.insert(0, "libs")
bot = commands.Bot(command_prefix="!>", owner_id=671791003065384987)

@bot.event
async def on_connect():
    print(f"\n > Began signing into Discord as {bot.user}")

@bot.event
async def on_ready():
    print(f" > Finished signing into Discord as {bot.user}\n")

    bot.remove_command("help")
    bot.load_extension("cogs.help")
    bot.load_extension("cogs.key")
    bot.load_extension("cogs.vis")
    bot.load_extension("cogs.encryption")
    print(" > Finished loading cogs\n")

    game = Game(name="!>help")
    await bot.change_presence(status=Status.online, activity=game)

@bot.event
async def on_error(error):
    pass

bot.run(TOKEN)
