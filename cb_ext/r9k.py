from nextcord import *
from nextcord.ext import commands

import cb_ext.util as u
from cb_ext.util import db

class REAL9000(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def check(message, edited=False):
        if message.channel.id == 960637529365831700:
            ref = db.reference("/casbot/r9k/")
            content = message.content.lower()

            if ";;;" in content:
                await message.delete()
        
            else:
                filtered = ''.join(filter(set('abcdefghijklmnopqrstuvwxyz').__contains__, message.content.lower()))
                if filtered.len() == 0 or filtered in ref.get("data"):
                    await message.delete()
                    # possibly add message or punishment here
                else:
                    new_data = ref.get("data") + filtered + ";;;"
                    ref.set("data", new_data)

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.check(message)

    @commands.Cog.listener()
    async def on_message_edited(self, message):
        await self.check(message, True)