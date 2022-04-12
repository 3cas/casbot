from nextcord import *
from nextcord.ext import commands
from time import sleep

import cb_ext.util as u
from cb_ext.util import db

# format of server: info vc
# REAL: "Members: X"
count_guilds = {929931487279718490: 935686520743014471}

async def check(message):
    if message.channel.id == 960637529365831700:
        ref = db.reference("/casbot/r9k/data")
        content = message.content.lower()

        if ";;;" in content or "?mute" in content:
            await message.delete()
    
        else:
            filtered = ''.join(filter(set('abcdefghijklmnopqrstuvwxyz').__contains__, message.content.lower()))
            if len(filtered) == 0 or filtered+";;;" in ref.get():
                if filtered not in ["goblin"]:
                    author = message.author
                    await message.delete()
                    # await author.timeout(timedelta(minutes=5), "Sent duplicate message in #REAL9000")
                    
                    
            else:
                new_data = ref.get() + filtered + ";;;"
                ref.set(new_data)

class RealServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        await check(message)

    @commands.Cog.listener()
    async def on_message_edit(self, message):
        await check(message)

    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            for guild_id in count_guilds:
                try:
                    guild = await self.bot.get_guild(guild_id)
                    channel = await self.bot.get_channel(count_guilds[guild_id])
                    await channel.edit(name = str(guild.member_count)+" members")
                except:
                    None
            
            sleep(10)

