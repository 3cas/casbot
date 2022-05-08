import re
from nextcord import *
from nextcord.ext import commands
from requests import get, post

import utility as u
from utility import db

try:
    import INIT_ENV  # type: ignore
except:
    None

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="I LOVE LEAN!!!!", guild_ids=u.mains)
    async def lean(self, interaction: Interaction):
        await interaction.response.send_message("**I LOVE LEAN!!!!**")

    @slash_command(description="Tests database", guild_ids=u.mains)
    async def datatest(self, interaction: Interaction):
        await interaction.response.send_message(db.reference("/test/").get())

    @slash_command(description="Gets a random Kanye quote", guild_ids=u.mains)
    async def kanyequote(self, interaction: Interaction):
        quote = get("https://api.kanye.rest/").json()["quote"]
        embed = Embed(color=Color.from_rgb(0, 0, 0), title="Kanye Quote", description=f"\"{quote}\"\n\t- Kanye West")
        await interaction.response.send_message(embed=embed)

    @slash_command(description="Gets a random neko image", guild_ids=u.mains)
    async def neko(self, interaction: Interaction):
        neko_img = get("https://nekos.best/api/v1/nekos").json()["url"]
        await interaction.response.send_message(neko_img)

    @slash_command(description="Generates text continuations using AI - [DISABLED]", guild_ids=u.mains)
    async def textgen(
        self, 
        interaction: Interaction, 
        start: str = SlashOption(name="start", description="Text to start with", required=True)
    ):

        text = post(
            "https://api.deepai.org/api/text-generator",
            data={'text': start},
            headers={'api-key': u.deepai_key}
        ).json()["output"]

        await interaction.response.send_message(text)

    @slash_command(description="Sets and retrives per-user notes", guild_ids=u.mains)
    async def usernote(self):
        None

    @usernote.subcommand(name="get", description="Get someone's user note")
    async def get_name(
        self, 
        interaction: Interaction,
        user: User = SlashOption(name="user", description="User to retrieve note of", required=False),
    ):
        if not user:
            user = interaction.user

        try:
            ref = db.reference("/casbot/usernotes/"+str(user.id))
            await interaction.response.send(f":paper: User note for **{user.name}**:\n> {ref.get()}")
        except Exception as e:
            await interaction.response.send(":x: ERROR: "+str(e))

    @usernote.subcommand(name="set", description="Set your own user note (This will overwrite the old one)")
    async def set_name(
        self,
        interaction: Interaction,
        note: str = SlashOption(name="note", description="The new note you want to change to", required=True)
    ):
        try:
            ref = db.reference("/casbot/usernotes/"+str(interaction.user.id))
            ref.set(note)
            await interaction.response.send(f":white_check_mark: User note for **{interaction.user.name}** set to \"{note}\"")
        except Exception as e:
            await interaction.response.send(":x: ERROR: "+str(e))

    @slash_command(description="Sends colored code block text using ANSI codes", guild_ids=u.mains)
    async def colortext(
        self,
        interaction: Interaction,
        text: str = SlashOption(name="text", description="Text you want to colorize", required=True),
        style: str = SlashOption(name="format", description="Normal, bold, or underline", required=False, choices=["normal", "bold", "underline"]),
        color: str = SlashOption(name="color", description="Color of the text", required=False, choices=["gray", "red", "green", "yellow", "blue", "pink", "cyan", "white"]),
        background: str = SlashOption(name="background", description="Color of the background/highlight", required=False, choices=["firefly dark blue", "orange", "marble blue", "grayish turquoise", "gray", "indigo", "light gray", "white"])
    ):
        color_string = f"\u001b[{style if style else '0'}{';'+color if color else ''}{';'+background if background else ''}m{text}"
        await interaction.response.send_message(f"Preview of your text:\n```ansi\n{color_string}\n```\n\nCopy this to use it elsewhere:\n```\n\\`\\`\\`ansi\n{color_string}\n\\`\\`\\`\n```")

def setup(bot):
    bot.add_cog(Misc(bot))