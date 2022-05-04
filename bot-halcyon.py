from nextcord import *
from nextcord.ext import commands
import logging
from os import getenv

import utility as u
from utility import debug_webhook as debug
from utility import db

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="ha!", description="Halcyon is a soon-to-be-public moderation bot, designed to be a fully free alternative to common Discord moderation bots. It is currently in development, and a work in progress. Developed with <3 by CAS#0001.", owner_ids=u.owners, intents=intents)

logging.basicConfig(level=logging.INFO)

cogs = ["test", "core", "settings"]
for cog in cogs:
    try:
        bot.load_extension("halcyon-"+cog)
    except Exception as e:
        debug.send("**Halcyon:** Error in cog `"+cog+"`: "+str(e))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    debug.send("**Halcyon:** Bot has started successfully")

    status_types = {"online": Status.online, "dnd": Status.dnd, "idle": Status.idle, "invisible": Status.invisible}
    activity_types = {"playing": ActivityType.playing, "streaming": ActivityType.streaming, "listening to": ActivityType.listening, "watching": ActivityType.watching, "competing in": ActivityType.competing}

    ref = db.reference("/halcyon/data/presence/")
    status_type = ref.child("statusType").get()
    activity_type = ref.child("activityType").get()
    activity_name = ref.child("activityValue").get()

    await bot.change_presence(status=status_types[status_type], activity=Activity(name=activity_name, type=activity_types[activity_type]))

    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('ha!hello'):
        await message.channel.send('Hello!')

try:
    import INIT_ENV  # type: ignore
except:
    None

TOKEN = getenv("HALCYON_TOKEN")

try:
    bot.run(TOKEN)
except Exception as e:
    debug.send("**Halcyon:** MAIN ERROR: "+str(e))
