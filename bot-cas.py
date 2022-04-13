from nextcord import *
from nextcord.ext import commands
import logging
from os import getenv

import cb_ext.util as u
from cb_ext.util import debug_webhook as debug

from cb_ext.dev import Developer
from cb_ext.personal import RealServer
from cb_ext.misc import Misc

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="c!", description="CASbot is a test bot created by CAS, aka >>#0001.", owner_ids=u.owners, intents=intents)

logging.basicConfig(level=logging.INFO)

cogs = ["dev", "misc", "personal", "mcount"]
for cog in cogs:
    try:
        bot.load_extension("cb_ext."+cog)
    except Exception as e:
        debug.send("**CASbot:** Error in cog "+cog+": "+str(e))

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
    import z_private  # type: ignore
except:
    None

TOKEN = getenv("CASBOT_TOKEN")

try:
    bot.run(TOKEN)
except Exception as e:
    debug.send("**CASbot:** MAIN ERROR: "+str(e))
