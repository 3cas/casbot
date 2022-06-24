from nextcord import *
from nextcord.ext import commands
from nextcord.ext import tasks

import utility as u
from utility import db

import datetime
import re

# Personal cog: For use in CAS's Discord servers, including moderation features and one-off functionality

async def r9k_check(message):
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

count_guilds = {929931487279718490: 935686520743014471}
mod = 930571601508966410

class Personal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.refresh_member_count.start()

    def cog_unload(self):
        self.refresh_member_count.cancel()

    @slash_command(description="Mutes (times out) a given member", guild_ids=u.moderated)
    @commands.has_role(mod)
    async def mute(
        self, 
        interaction: Interaction, 
        member: Member = SlashOption(name="user", description="User to time out", required=True), 
        duration: str = SlashOption(name="duration", description="Duration of timeout", required=True),
        reason: str = SlashOption(name="reason", description="Reason for timeout", required=False)
    ):
        days = 0
        seconds = 0
        
        duration2 = ""
        for char in duration:
            if char in "1234567890smhdwmy":
                duration2 += char
        
        while duration2[0] not in "1234567890":
            duration2 = duration2[1:]

        while duration2[-1] not in "smhdwmy":
            duration2 = duration2[:-2]

        values = re.split("s|m|h|d|w|m|y", duration2)
        units = re.split("1|2|3|4|5|6|7|8|9|0", duration2)
        
        for i in range(len(values)):
            values[i] = int(values[i])

            if units[i] == "s":
                seconds += values[i]
            elif units[i] == "m":
                seconds += values[i] * 60
            elif units[i] == "h":
                seconds += values[i] * 3600
            elif units[i] == "d":
                days += values[i]
            elif units[i] == "w":
                days += values[i] * 7
            elif units[i] == "m":
                days += values[i] * 30
            elif units[i] == "y":
                days += values[i] * 365

        delta = datetime.timedelta(seconds=seconds, days=days)

        if not reason:
            reason = "none"

        await member.timeout(delta, reason)
        await interaction.send(f"Timed out **{member.name}** for **{days} days** and **{seconds} seconds**.")

    @commands.Cog.listener("on_message")
    async def check_sent(self, message):
        await r9k_check(message)

    @tasks.loop(seconds = 10.0)
    async def refresh_member_count(self):
        try:
            for guild_id in count_guilds:
                guild = self.bot.get_guild(guild_id)
                channel = guild.get_channel(count_guilds[guild_id])
                await channel.edit(name = str(len(guild.humans))+" members")
        except:
            None
        
def setup(bot):
    bot.add_cog(Personal(bot))