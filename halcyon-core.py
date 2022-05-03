from nextcord import *
from nextcord.ext import commands
from nextcord.utils import find
from requests import get, post

import utility as u
from utility import db

try:
    import INIT_ENV  # type: ignore
except:
    None

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.event
    async def on_guild_join(guild):
        general = find(lambda x: x.name == "general",  guild.text_channels)
        if general and general.permissions_for(guild.me).send_messages:
            await general.send(f"Hello {guild.name}!\n\nThank you for adding Halcyon. The bot is currently still in development, and no moderation features are actually available. If you have any questions or suggestions, please contact me at CAS#0001.\n\nThanks,\nCAS-14")

        

    @slash_command(description="I LOVE LEAN!!!!", guild_ids=u.mains)
    async def lean(self, interaction: Interaction):
        await interaction.response.send_message("**I LOVE LEAN!!!!**")

    @slash_command(description="Gets a random Kanye quote", guild_ids=u.mains)
    async def kanyequote(self, interaction: Interaction):
        quote = get("https://api.kanye.rest/").json()["quote"]
        embed = Embed(color=Color.from_rgb(0, 0, 0), title="Kanye Quote", description=f"\"{quote}\"\n\t- Kanye West")
        await interaction.response.send_message(embed=embed)

    @slash_command(description="Gets a random neko image", guild_ids=u.mains)
    async def neko(self, interaction: Interaction):
        neko_img = get("https://nekos.best/api/v1/nekos").json()["url"]
        await interaction.response.send_message(neko_img)

    
def setup(bot):
    bot.add_cog(Core(bot))