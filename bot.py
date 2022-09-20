import nextcord
from nextcord.ext import commands
import logging
import json
import sys
import os
from firebase_admin import credentials, initialize_app, db
import dotenv

from cogs.dev import Developer
from cogs.misc import Miscellaneous

def run(TOKEN: str, debug: nextcord.SyncWebhook, db):
    with open("config.json", "r") as f:
        config = json.load(f)
    
    owners = config["owners"]
    guilds = config["guilds"]

    intents = nextcord.Intents.all()
    intents.members = True

    bot = commands.Bot(description="CASbot is a test bot created by weirdcease#0001", owner_ids=owners, intents=intents)

    #logging.basicConfig(level=logging.INFO)

    @bot.event
    async def on_ready():
        print(f'CASBOT: We have logged in as {bot.user}')
        debug.send("**CASbot:** Bot has started successfully")

        ref = db.reference("/casbot/data/presence/")
        status_type = ref.child("statusType").get()
        activity_type = ref.child("activityType").get()
        activity_name = ref.child("activityValue").get()

        status_types = {
            "online": nextcord.Status.online, 
            "dnd": nextcord.Status.dnd, 
            "idle": nextcord.Status.idle, 
            "invisible": nextcord.Status.invisible
        }

        activity_types = {
            "playing": nextcord.ActivityType.playing, 
            "streaming": nextcord.ActivityType.streaming, 
            "listening to": nextcord.ActivityType.listening, 
            "watching": nextcord.ActivityType.watching, 
            "competing in": nextcord.ActivityType.competing
        }

        await bot.change_presence(status=status_types[status_type], activity=nextcord.Activity(name=activity_name, type=activity_types[activity_type]))

        print("\nBot in guilds:")
        async for guild in bot.fetch_guilds():
            print(f"{guild.name} [{guild.id}]")
            guilds.append(guild.id)
        print()

        for cog in (Developer, Miscellaneous):
            cog.guilds = guilds
            bot.add_cog(cog(bot, db))

    try:
        bot.run(TOKEN)
    except Exception as e:
        debug.send("**CASbot:** MAIN ERROR: "+str(e))

if __name__ == "__main__":
    os.chdir(sys.path[0])

    if len(sys.argv) > 1 and sys.argv[1] == "--no-env":
        print("Not loading .env file!")
    else:
        dotenv.load_dotenv() # .env is not needed if using bot controller to run file

    TOKEN = os.getenv("CASBOT_TOKEN")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")
    FIREBASE_KEY = json.loads(os.getenv("FIREBASE_KEY"), strict=False)

    debug_webhook = nextcord.SyncWebhook.from_url(WEBHOOK_URL)

    cred = credentials.Certificate(FIREBASE_KEY)
    initialize_app(cred, {
        'databaseURL': 'https://casbot-db-default-rtdb.firebaseio.com'
    })

    run(TOKEN, debug_webhook, db)
