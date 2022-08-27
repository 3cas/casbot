import nextcord
import requests
import dotenv

import utility

dotenv.load_dotenv()

# Miscellaneous cog: for miscellaneous fun features like accessing the Kanye API and Neko API

class Miscellaneous(nextcord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Gets a random Kanye quote", guild_ids=utility.mains)
    async def kanyequote(self, interaction: nextcord.Interaction):
        quote = requests.get("https://api.kanye.rest/").json()["quote"]
        embed = nextcord.Embed(color=nextcord.Color.from_rgb(0, 0, 0), title="Kanye Quote", description=f"\"{quote}\"\n\t- Kanye West")
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(description="Gets a random anime catgirl", guild_ids=utility.mains)
    async def neko(self, interaction: nextcord.Interaction):
        neko_img = requests.get("https://nekos.best/api/v1/nekos").json()["url"]
        await interaction.response.send_message(neko_img)

    @nextcord.slash_command(description="Gets a random doge (shibe) image", guild_ids=utility.mains)
    async def doge(self, interaction: nextcord.Interaction):
        doge_img = requests.get("http://shibe.online/api/shibes").json()[0]
        await interaction.response.send_message(doge_img)

    @nextcord.slash_command(description="Sets and retrives per-user notes", guild_ids=utility.mains)
    async def usernote(self):
        None

    @usernote.subcommand(name="get", description="Get someone's user note")
    async def get_name(
        self, 
        interaction: nextcord.Interaction,
        user: nextcord.User = nextcord.SlashOption(name="user", description="User to retrieve note of", required=False),
    ):
        if not user:
            user = interaction.user

        try:
            ref = utility.db.reference("/casbot/usernotes/"+str(user.id))
            await interaction.response.send_message(f":paper: User note for **{user.name}**:\n> {ref.get()}")
        except Exception as e:
            await interaction.response.send_message(":x: ERROR: "+str(e))

    @usernote.subcommand(name="set", description="Set your own user note (This will overwrite the old one)")
    async def set_name(
        self,
        interaction: nextcord.Interaction,
        note: str = nextcord.SlashOption(name="note", description="The new note you want to change to", required=True)
    ):
        try:
            ref = utility.db.reference("/casbot/usernotes/"+str(interaction.user.id))
            ref.set(note)
            await interaction.response.send_message(f":white_check_mark: User note for **{interaction.user.name}** set to \"{note}\"")
        except Exception as e:
            await interaction.response.send_message(":x: ERROR: "+str(e))

    @nextcord.slash_command(description="Sends colored code block text using ANSI codes", guild_ids=utility.mains)
    async def colortext(
        self,
        interaction: nextcord.Interaction,
        text: str = nextcord.SlashOption(name="text", description="Text you want to colorize - You can use %n to insert a new line", required=True),
        style: str = nextcord.SlashOption(name="format", description="Bold or underline (optional)", required=False, choices=["bold", "underline"]),
        color: str = nextcord.SlashOption(name="color", description="Color of the text (optional)", required=False, choices=["gray", "red", "green", "yellow", "blue", "pink", "cyan", "white"]),
        background: str = nextcord.SlashOption(name="background", description="Color of the background/highlight (optional)", required=False, choices=["firefly dark blue", "orange", "marble blue", "grayish turquoise", "gray", "indigo", "light gray", "white"])
    ):
        text = "\n".join(text.split("%n"))

        style = {None: 0, "bold": 1, "underline": 4}[style]
        color = {None: None, "gray": 30, "red": 31, "green": 32, "yellow": 33, "blue": 34, "pink": 35, "cyan": 36, "white": 37}[color]
        background = {None: None, "firefly dark blue": 40, "orange": 41, "marble blue": 42, "grayish turquoise": 43, "gray": 44, "indigo": 45, "light gray": 46, "white": 47}[background]

        color_string = f"\u001b[{style}{';'+str(color) if color else ''}{';'+str(background) if background else ''}m{text}"
        await interaction.response.send_message(f"Preview of your text:\n```ansi\n{color_string}\n```\nCopy everything below this to use it elsewhere:\n\n\`\`\`ansi\n{color_string}\n\`\`\`")

def setup(bot):
    bot.add_cog(Miscellaneous(bot))