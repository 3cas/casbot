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
    #tl = bot.get_guild(957025882399195156)
    #cas = tl.get_member(743340045628342324)

    #mute = tl.get_role(957069369119211620)
    #botr = tl.get_role(957064198712594452)
   # dev = tl.get_role(957065009509330984)

    #print(f"Member: {cas} in {tl}\nRemoving: {mute}\nAdding: {botr}, {dev}")

    #await cas.remove_roles(mute)
    #await cas.add_roles(botr, dev)

    chan = bot.get_channel(957060354582650961)
    for i in range(100):
        await chan.send("NERD!")

    print("DONE")

bot.run(TOKEN)

