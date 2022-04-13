from nextcord import *
from nextcord.ext import commands
from nextcord.ext import tasks

import cb_ext.util as u
from cb_ext.util import db

# format of server: info vc
# REAL: "Members: X"

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
        #self.count_guilds = {929931487279718490: 935686520743014471}
        #self.refresh_member_count.start()

    #def cog_unload(self):
        #self.refresh_member_count.cancel()

    @commands.Cog.listener()
    async def on_message(self, message):
        await check(message)

    @commands.Cog.listener()
    async def on_message_edit(self, message):
        await check(message)

"""
    @tasks.loop(seconds = 10.0)
    async def refresh_member_count(self):
        try:
            for guild_id in self.count_guilds:
                guild = self.bot.get_guild(929931487279718490)
                channel = guild.get_channel(self.count_guilds[guild_id])
                await channel.edit(name = str(len(guild.humans))+" members")
        except:
            None
"""
        
def setup(bot):
    bot.add_cog(RealServer(bot))