from nextcord import *
from nextcord.ext import commands

import cb_ext.util as u
from cb_ext.util import db

class REAL9000(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def check(message, edited=False):
        if message.channel.id == 960637529365831700:
            ref = db.reference("/casbot/r9k/data")
            content = message.content.lower()

            if ";;;" in content:
                await message.delete()
        
            else:
                filtered = ''.join(filter(set('abcdefghijklmnopqrstuvwxyz').__contains__, message.content.lower()))
                if filtered.len() == 0 or filtered in ref.get():
                    await message.delete()
                    # possibly add message or punishment here
                else:
                    new_data = ref.get() + filtered + ";;;"
                    ref.set(".", new_data)

    @commands.Cog.listener("on_message")
    async def check_sent(self, message):
        if message.channel.id == 960637529365831700:
            ref = db.reference("/casbot/r9k/")
            content = message.content.lower()

            if ";;;" in content:
                await message.delete()
        
            else:
                filtered = ''.join(filter(set('abcdefghijklmnopqrstuvwxyz').__contains__, message.content.lower()))
                if len(filtered) == 0 or filtered in ref.get()[0]:
                    await message.delete()
                    # possibly add message or punishment here
                else:
                    new_data = ref.get() + filtered + ";;;"
                    ref.set(".", new_data)

    @commands.Cog.listener("on_message_edited")
    async def check_edited(self, message):
        await self.check(message, True)