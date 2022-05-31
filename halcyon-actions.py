from nextcord import *
from nextcord.ext import commands
from requests import get, post

import utility as u
from utility import db

try:
    import INIT_ENV  # type: ignore
except:
    None

class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="ban a user", guild_ids=u.mains)
    async def lean(self, interaction: Interaction):
        await interaction.response.send_message("Test response")


def setup(bot):
    bot.add_cog(Actions(bot))
