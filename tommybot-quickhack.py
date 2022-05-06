from nextcord import *
from nextcord.ext import commands
from os import getenv
import logging
import random
import requests

try:
    import INIT_ENV  # type: ignore
except:
    None

prefix = "t?"

intents = Intents.default()
intents.members = True

TOKEN = getenv("TOMMYBOT_TOKEN")

WEBHOOK_URL = getenv("DEBUG_WEBHOOK")
debug = SyncWebhook.from_url(WEBHOOK_URL)

bot = commands.Bot(command_prefix=prefix, description="Mecha Tommy is a custom bot made for Tommylore and Sas, made by >>#0001.", intents=intents, owner_ids={956698441361260567,743340045628342324,901978388829450291})

logging.basicConfig(level=logging.INFO)

bot.remove_command("help")

@bot.event
async def on_ready():
    tl = bot.get_guild(957025882399195156)
    #cas = tl.get_member(743340045628342324)

    chan = bot.get_channel(957060580060041236)
    ari = tl.get_member(688794979573039104)
    await chan.send("<@&957055678961320041> <@&964297071928688691> <@&957266645167013928> <@&970315000176582736> <@&957068494745251851> timmny")
    #await ari.kick()

    print("DONE")

bot.run(TOKEN)

