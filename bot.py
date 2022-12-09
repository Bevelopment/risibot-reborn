# Import the necessary libraries.
import disnake
from disnake.ext import commands

from configs import BOT_TOKEN

# Creating a commands.Bot() instance, and assigning it to "bot"
bot = commands.Bot()

# When the bot is ready, run this code.
@bot.event
async def on_ready():
    print("The bot is ready!")


@bot.slash_command(guild_ids=[758956846551007233])  # Your server IDs go here.
async def ping(inter):
    await inter.response.send_message("Pong!")


@bot.slash_command()
async def server(inter):
    await inter.response.send_message(
        f"Server name: {inter.guild.name}\nTotal members: {inter.guild.member_count}"
    )


# Login to Discord with the bot's token.
bot.run(BOT_TOKEN)
