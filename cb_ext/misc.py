from nextcord import *
from nextcord.ext import commands
from requests import get, post

import cb_ext.util as u
from cb_ext.util import db

try:
    import z_private  # type: ignore
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

    @slash_command(description="Generates text continuations using AI", guild_ids=u.mains)
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

def setup(bot):
    bot.add_cog(Misc(bot))