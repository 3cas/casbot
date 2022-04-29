from nextcord import *
from nextcord.ext import commands
import logging
from os import getenv

import cb_ext.util as u
from cb_ext.util import debug_webhook as debug
from cb_ext.util import db

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="c!", description="CASbot is a test bot created by CAS#0001", owner_ids=u.owners, intents=intents)

logging.basicConfig(level=logging.INFO)

cogs = ["dev", "misc", "personal"]
for cog in cogs:
    try:
        bot.load_extension("cb_ext."+cog)
    except Exception as e:
        debug.send("**CASbot:** Error in cog "+cog+": "+str(e))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    debug.send("**CASbot:** Bot has started successfully")

    status_types = {"online": Status.online, "dnd": Status.dnd, "idle": Status.idle, "invisible": Status.invisible}
    activity_types = {"playing": ActivityType.playing, "streaming": ActivityType.streaming, "listening to": ActivityType.listening, "watching": ActivityType.watching, "competing in": ActivityType.competing}

    ref = db.reference("/casbot/data/presence/")
    status_type = ref.child("statusType").get()
    activity_type = ref.child("activityType").get()
    activity_name = ref.child("activityValue").get()

    await bot.change_presence(status=status_types[status_type], activity=Activity(name=activity_name, type=activity_types[activity_type]))

    

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
