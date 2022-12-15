import asyncio
import os

import disnake
from disnake.ext import commands, tasks

from configs import (
    ARCHIVE_CHANNEL,
    BOT_TOKEN,
    CLR_ERROR,
    CLR_SUCCESS,
    CLR_WARNING,
    GUILDS_TEST_ID,
    INVITE_LINK,
    KEEP_ALIVE_MESSAGE,
    LOGS_CHANNEL,
    STATUS_TASK,
    SUPPORT_LINK,
)

asyncio.sleep(5.9)  # to avoid discord rate limits
os.system("clear")
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True
# Creating a commands.Bot() instance, and assigning it to "bot"
bot = commands.Bot(
    command_prefix="!",
    command_sync_flags=command_sync_flags,
    test_guilds=GUILDS_TEST_ID,
)

# checking when the bot is ready
@bot.event
async def on_ready():
    print("-----------------------------")
    print("BOT PRESENCE")
    print("-----------------------------")
    print(f"Im logged in as {bot.user}")
    print(f"In {len(bot.guilds)} guilds")
    print(f"Disnake Version: {disnake.__version__}")
    print(f"Starting Status Task: {STATUS_TASK}")
    print(f"Keep alive message: {KEEP_ALIVE_MESSAGE}")

    print("-----------------------------")
    print("BOT ENVIRONMENT SETTINGS")
    print("-----------------------------")
    print(f"BOT_TOKEN: {BOT_TOKEN[10:]}*************{BOT_TOKEN[:10]}")
    print(f"STATUS_TASK: {STATUS_TASK}")
    print(f"GUILDS_TEST_ID: {GUILDS_TEST_ID}")
    print(f"LOGS_CHANNEL: {LOGS_CHANNEL}")
    print(f"ARCHIVE_CHANNEL: {ARCHIVE_CHANNEL}")
    print(f"SUPPORT_LINK: {SUPPORT_LINK}")
    print(f"INVITE_LINK: {INVITE_LINK}")

    print("-----------------------------")
    print("BOT COLOR SETTINGS")
    print("-----------------------------")
    print(f"CLR_SUCCESS: {CLR_SUCCESS}")
    print(f"CLR_WARNING: {CLR_WARNING}")
    print(f"CLR_ERROR: {CLR_ERROR}")
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
