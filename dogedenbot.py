from nextcord import *
from nextcord.ext import commands
import logging
from os import getenv

import utility as u
from utility import debug_webhook as debug

from requests import get

intents = Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="dd!", description="DogeDenBot is a Discord bot created for Doge Den by CAS#0001", owner_ids=u.owners, intents=intents)

logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    debug.send("**DogeDenBot:** Bot has started successfully")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('c!hello'):
        await message.channel.send('Hello!')

@slash_command(guild_ids=u.mains)
async def doge(self, interaction: Interaction):
    doge_img = get("http://shibe.online/api/shibes").json()[0]
    await interaction.response.send_message(doge_img)

try:
    import INIT_ENV  # type: ignore
except:
    None

TOKEN = getenv("DOGEDENBOT_TOKEN")

try:
    bot.run(TOKEN)
except Exception as e:
    debug.send("**DogeDenBot:** MAIN ERROR: "+str(e))
