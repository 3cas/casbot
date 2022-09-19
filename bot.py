from tkinter import Misc
import nextcord
from nextcord.ext import commands
import logging
import json

def run(TOKEN, debug: nextcord.SyncWebhook, db):
    with open("config.json", "r") as f:
        config = json.load(f)
    
    owners = config["owners"]
    guilds = config["guilds"]

    intents = nextcord.Intents.all()
    intents.members = True

    bot = commands.Bot(command_prefix="c!", description="CASbot is a test bot created by weirdcease#0001", owner_ids=owners, intents=intents)

    logging.basicConfig(level=logging.INFO)

    from cogs.dev import Developer
    from cogs.misc import Miscellaneous

    for cog in (Developer, Miscellaneous):
        cog.guilds = guilds
        bot.add_cog(cog(bot, db))

    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')
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

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        if message.content.startswith('c!hello'):
            await message.channel.send('Hello!')

    try:
        bot.run(TOKEN)
    except Exception as e:
        debug.send("**CASbot:** MAIN ERROR: "+str(e))

if __name__ == "__main__":
    import dotenv
    import os
    import firebase_admin

    dotenv.load_dotenv()

    TOKEN = os.getenv("CASBOT_TOKEN")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")
    FIREBASE_KEY = json.loads(os.getenv("FIREBASE_KEY"), strict=False)

    debug_webhook = nextcord.SyncWebhook.from_url(WEBHOOK_URL)

    cred = firebase_admin.credentials.Certificate(FIREBASE_KEY)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://casbot-db-default-rtdb.firebaseio.com'
    })

    run(TOKEN, debug_webhook, firebase_admin.db)
