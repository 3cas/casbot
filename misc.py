import discord
from discord.ext import commands
import requests
import json

with open("config.json", "r") as f:
    config = json.load(f)

# Miscellaneous cog: for miscellaneous fun features like accessing the Kanye API and Neko API

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Gets a random Kanye quote")
    async def kanyequote(self, interaction: discord.Interaction):
        quote = requests.get("https://api.kanye.rest/").json()["quote"]
        embed = discord.Embed(color=discord.Color.from_rgb(0, 0, 0), title="Kanye Quote", description=f"\"{quote}\"\n\t- Kanye West")
        await interaction.response.send_message(embed=embed)

    @commands.command(description="Gets a random anime catgirl")
    async def neko(self, interaction: discord.Interaction):
        neko_img = requests.get("https://nekos.best/api/v2/neko").json()["results"][0]["url"]
        await interaction.response.send_message(neko_img)

    @commands.command(description="Gets a random doge (shibe) image")
    async def doge(self, interaction: discord.Interaction):
        doge_img = requests.get("http://shibe.online/api/shibes").json()[0]
        await interaction.response.send_message(doge_img)

    # @discord.slash_command(description="Sets and retrives per-user notes")
    # async def usernote(self):
    #     None

    # @usernote.subcommand(name="get", description="Get someone's user note")
    # async def get_name(
    #     self, 
    #     interaction: discord.Interaction,
    #     user: discord.User = discord.SlashOption(name="user", description="User to retrieve note of", required=False),
    # ):
    #     print("CASBOT: Running /usernote get")

    #     if not user:
    #         user = interaction.user

    #     try:
    #         ref = self.db.reference("/casbot/usernotes/"+str(user.id))
    #         await interaction.response.send_message(f":paper: User note for **{user.name}**:\n> {ref.get()}")
    #     except Exception as e:
    #         await interaction.response.send_message(":x: ERROR: "+str(e))

    # @usernote.subcommand(name="set", description="Set your own user note (This will overwrite the old one)")
    # async def set_name(
    #     self,
    #     interaction: discord.Interaction,
    #     note: str = discord.SlashOption(name="note", description="The new note you want to change to", required=True)
    # ):
    #     print("CASBOT: Running /usernote set")

    #     try:
    #         ref = self.db.reference("/casbot/usernotes/"+str(interaction.user.id))
    #         ref.set(note)
    #         await interaction.response.send_message(f":white_check_mark: User note for **{interaction.user.name}** set to \"{note}\"")
    #     except Exception as e:
    #         await interaction.response.send_message(":x: ERROR: "+str(e))

    # @discord.slash_command(description="Sends colored code block text using ANSI codes")
    # async def colortext(
    #     self,
    #     interaction: discord.Interaction,
    #     text: str = discord.SlashOption(name="text", description="Text you want to colorize - You can use %n to insert a new line", required=True),
    #     style: str = discord.SlashOption(name="format", description="Bold or underline (optional)", required=False, choices=["bold", "underline"]),
    #     color: str = discord.SlashOption(name="color", description="Color of the text (optional)", required=False, choices=["gray", "red", "green", "yellow", "blue", "pink", "cyan", "white"]),
    #     background: str = discord.SlashOption(name="background", description="Color of the background/highlight (optional)", required=False, choices=["firefly dark blue", "orange", "marble blue", "grayish turquoise", "gray", "indigo", "light gray", "white"])
    # ):
    #     print("CASBOT: Running /colortext")

    #     text = "\n".join(text.split("%n"))

    #     style = {None: 0, "bold": 1, "underline": 4}[style]
    #     color = {None: None, "gray": 30, "red": 31, "green": 32, "yellow": 33, "blue": 34, "pink": 35, "cyan": 36, "white": 37}[color]
    #     background = {None: None, "firefly dark blue": 40, "orange": 41, "marble blue": 42, "grayish turquoise": 43, "gray": 44, "indigo": 45, "light gray": 46, "white": 47}[background]

    #     color_string = f"\u001b[{style}{';'+str(color) if color else ''}{';'+str(background) if background else ''}m{text}"
    #     await interaction.response.send_message(f"Preview of your text:\n```ansi\n{color_string}\n```\nCopy everything below this to use it elsewhere:\n\n\`\`\`ansi\n{color_string}\n\`\`\`")