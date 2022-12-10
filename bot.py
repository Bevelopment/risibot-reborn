import asyncio
import os

import disnake
from disnake.ext import commands, tasks

from configs import BOT_TOKEN, GUILD_TEST_ID, STATUS_TASK

asyncio.sleep(5.9)  # to avoid discord rate limits
os.system("clear")
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True
# Creating a commands.Bot() instance, and assigning it to "bot"
bot = commands.Bot(
    command_prefix="!",
    command_sync_flags=command_sync_flags,
    test_guilds=[GUILD_TEST_ID],
)

# checking when the bot is ready
@bot.event
async def on_ready():
    print(f"Im logged in as {bot.user}")
    print(f"In {len(bot.guilds)} guilds")
    print(f"Disnake Version: {disnake.__version__}")
    print(f"Starting Status Task: {STATUS_TASK}")
    print("-----------------------------")
    status_task.start()


# Setup the game status task of the bot
# change the minutes to what ever you want, remove if you want
@tasks.loop(minutes=5.0)
async def status_task():
    # change the 'ActivityType.playing' to listening, watching, streaming, playing, competing
    await bot.change_presence(
        activity=disnake.Activity(type=disnake.ActivityType.playing, name=STATUS_TASK)
    )


@bot.slash_command()
async def server(inter):
    await inter.response.send_message(
        f"Server name: {inter.guild.name}\n"
        + f"Total members: {inter.guild.member_count}"
    )


# loading all extensions in the cogs folder
if __name__ in "__main__":
    py_path = f"cogs"
    folder = f"cogs"
    for name in os.listdir(folder):
        if name.endswith(".py") and os.path.isfile(
            f"cogs/{name}"
        ):  # finding all python files (.py)
            bot.load_extension(f"{py_path}.{name[:-3]}")

# running the bot with the token
bot.run(BOT_TOKEN)
