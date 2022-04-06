from nextcord import *
from nextcord.ext import commands
from datetime import timedelta

import cb_ext.util as u
from cb_ext.util import db

async def check(message, edited=False):
    if message.channel.id == 960637529365831700:
        ref = db.reference("/casbot/r9k/data")
        content = message.content.lower()

        if ";;;" in content or "?mute" in content:
            await message.delete()
    
        else:
            filtered = ''.join(filter(set('abcdefghijklmnopqrstuvwxyz').__contains__, message.content.lower()))
            if len(filtered) == 0 or filtered+";;;" in ref.get():
                if filtered not in ["goblin"]:
                    await message.author.timeout(timedelta(minutes=5), "Sent duplicate message in #REAL9000")
                    await message.delete()
                    
            else:
                new_data = ref.get() + filtered + ";;;"
                print(new_data)
                ref.set(new_data)

class REAL9000(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def check_sent(self, message):
        await check(message)

    @commands.Cog.listener("on_message_edited")
    async def check_edited(self, message):
        await check(message, True)