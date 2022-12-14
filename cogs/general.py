import random

import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import message_command, slash_command, user_command

from configs import INVITE_LINK, SUPPORT_LINK


class General(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @slash_command(name="ping", description="Check if the bot is alive")
    async def ping(self, inter):
        embed = disnake.Embed(
            title=":ping_pong: Pong!",
            description=f"{round(self.bot.latency * 1000)}ms.",
            color=disnake.Color.green(),
        )
        await inter.response.send_message(embed=embed)

    @slash_command(name="invite", description="invite bot on new serv")
    async def invite(self, inter):
        await inter.author.send(f"Voici ton lien d'invitation: {INVITE_LINK}")

    @slash_command(
        name="support",
        description="let newcomers to reach us and let us answer their needs",
    )
    async def support(self, inter):
        await inter.author.send(
            f"Rendez-vous sur le discord du support : {SUPPORT_LINK} !"
        )

    @slash_command(name="bienvenue", description="Welcome the newcommer")
    async def bienvenue(self, inter):
        await inter.response.send_message(
            f"Bienvenue sur {inter.guild.name}, {inter.user.name} !"
        )

    @slash_command(name="poll", description="Create a poll that users can react to")
    async def poll(
        self,
        inter,
        emoji_1: disnake.Emoji,
        emoji_2: disnake.Emoji,
        emoji_3: disnake.Emoji,
        title,
    ):
        embed = disnake.Embed(
            title=title,
            description="A new poll has been created!",
            color=disnake.Color.green(),
        )
        embed.set_footer(text=f"Poll created by: {inter.author} • React to vote!")
        embed_message = await inter.send(embed=embed)
        await embed_message.add_reaction(emoji_1)
        await embed_message.add_reaction(emoji_2)
        await embed_message.add_reaction(emoji_3)

    @slash_command(name="botinfo", description="Get some information about the bot")
    async def botinfo(self, inter):
        embed = disnake.Embed(
            title=f"Name: {self.bot.user}",
            description=f"ID: {self.bot.user.id}",
            color=disnake.Color.green(),
        )
        embed.add_field(name="Dev lead", value="Tarto#3361")
        embed.add_field(name="Dev", value="Darionnette#3470")
        embed.add_field(name="Testing", value="Prochak#3662")

        embed.add_field(name="Disnake Version", value=f"{disnake.__version__}")
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        await inter.send(embed=embed)

    @slash_command(name="serverinfo", description="Get some info on the current server")
    async def serverinfo(self, inter):
        server = inter.guild
        roles = [x.name for x in server.roles]
        role_length = len(roles)
        if role_length > 50:
            roles = roles[:50]
            roles.append(f">> Displaying[50/{len(roles)}] Roles")
        roles = ", ".join(roles)
        channels = len(server.channels)
        time = str(server.created_at)
        time = time.split(" ")
        time = time[0]

        embed = disnake.Embed(
            title="**Server Name:**", description=f"{server}", color=0x42F56C
        )
        try:
            embed.set_thumbnail(url=server.icon_url)
        except:
            print(f"No server icon found for {server.name}")
        embed.add_field(name="Server ID", value=server.id)
        embed.add_field(name="Member Count", value=server.member_count)
        embed.add_field(
            name="Boosts", value=f"{str(inter.guild.premium_subscription_count)}"
        )
        embed.add_field(name="Text/Voice Channels", value=f"{channels}")
        embed.add_field(name=f"Roles ({role_length})", value=roles)
        embed.set_footer(text=f"Created at: {time}")
        await inter.send(embed=embed)

    @slash_command(name="random", description="Generate a random number")
    async def rng(self, inter, lower_number: int, upper_number: int):
        embed = disnake.Embed(
            title=":game_die: You rolled:",
            description=f"{random.randint(lower_number, upper_number)}",
            color=disnake.Color.green(),
        )
        await inter.send(embed=embed)

    @slash_command(name="combo", description="Generate Combinations from a string")
    async def combo(self, inter, string: str):
        complete_list = []
        for current in range(len(string)):
            a = [i for i in string]
            for y in range(current):
                a = [x + i for i in string for x in a]
            complete_list += a
            with open("combos.txt", "w") as f:
                for item in complete_list:
                    f.write(item + "\n")
        await inter.send(file=disnake.File("combos.txt"))


def setup(bot):
    bot.add_cog(General(bot))
    print(f"> Extension {__name__} is ready")
