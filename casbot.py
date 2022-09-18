import nextcord
from nextcord.ext import commands
import logging
import os
import dotenv

import utility

dotenv.load_dotenv()

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="c!", description="CASbot is a test bot created by CAS#0001", owner_ids=utility.owners, intents=intents)

logging.basicConfig(level=logging.INFO)

cogs = ["dev", "misc"]
for cog in cogs:
    try:
        bot.load_extension("casbot-"+cog)
    except Exception as e:
        utility.debug_webhook.send("**CASbot:** Error in cog `"+cog+"`: "+str(e))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    utility.debug_webhook.send("**CASbot:** Bot has started successfully")

    ref = utility.db.reference("/casbot/data/presence/")
    status_type = ref.child("statusType").get()
    activity_type = ref.child("activityType").get()
    activity_name = ref.child("activityValue").get()

    await bot.change_presence(status=utility.status_types[status_type], activity=nextcord.Activity(name=activity_name, type=utility.activity_types[activity_type]))

    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('c!hello'):
        await message.channel.send('Hello!')

try:
    bot.run(os.getenv("CASBOT_TOKEN"))
except Exception as e:
    utility.debug_webhook.send("**CASbot:** MAIN ERROR: "+str(e))
