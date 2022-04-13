from nextcord import *
from nextcord.ext import commands
from nextcord.ext import tasks

import cb_ext.util as u

class MemberCountReal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.count_guilds = {929931487279718490: 935686520743014471}
        self.refresh_member_count.start()

    def cog_unload(self):
        self.refresh_member_count.cancel()

    @tasks.loop(seconds=10.0)
    async def refresh_member_count(self):
        try:
            for guild_id in self.count_guilds:
                guild = self.bot.get_guild(929931487279718490)
                channel = guild.get_channel(self.count_guilds[guild_id])
                await channel.edit(name=str(len(guild.humans))+" members")
        except:
            None

def setup(bot):
    bot.add_cog(MemberCountReal(bot))
