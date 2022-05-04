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

    @commands.Cog.listener()
    async def on_guild_join(guild):
        general = find(lambda x: x.name == "general",  guild.text_channels)
        if general and general.permissions_for(guild.me).send_messages:
            await general.send(f"Hello {guild.name}!\n\nThank you for adding Halcyon. The bot is currently still in development, and no moderation features are actually available. If you have any questions or suggestions, please contact me at CAS#0001.\n\nThanks,\nCAS-14")
    
def setup(bot):
    bot.add_cog(Core(bot))