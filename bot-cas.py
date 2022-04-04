from nextcord import *
from nextcord.ext import commands
import logging
from os import getenv

import cb_ext.util as u
from cb_ext.util import debug_webhook as debug

from cb_ext.owner import Owner
from cb_ext.r9k import REAL9000
from cb_ext.misc import Misc

bot = commands.Bot(command_prefix="c!", description="CASbot is a test bot created by CAS, aka >>#0001.", owner_ids=u.owners)

logging.basicConfig(level=logging.INFO)

bot.add_cog(Owner(bot))
# bot.add_cog(REAL9000(bot))
bot.add_cog(Misc(bot))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    debug.send("**CASbot:** Bot has started successfully")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('c!hello'):
        await message.channel.send('Hello!')

try:
    import z_private
except:
    None

TOKEN = getenv("CASBOT_TOKEN")

try:
    bot.run(TOKEN)
except Exception as e:
    debug.send("**CASbot:** MAIN ERROR: "+str(e))
