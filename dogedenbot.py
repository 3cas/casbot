import nextcord
import logging
import os
import requests

import utility

intents = nextcord.Intents.all()
intents.members = True

bot = nextcord.ext.commands.Bot(command_prefix="dd!", description="DogeDenBot is a Discord bot created for Doge Den by CAS#0001", owner_ids=utility.owners, intents=intents)

logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    utility.debug_webhook.send("**DogeDenBot:** Bot has started successfully")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('c!hello'):
        await message.channel.send('Hello!')

@nextcord.slash_command(guild_ids=utility.mains)
async def doge(self, interaction: nextcord.Interaction):
    doge_img = requests.get("http://shibe.online/api/shibes").json()[0]
    await interaction.response.send_message(doge_img)

try:
    bot.run(os.getenv("DOGEDENBOT_TOKEN"))
except Exception as e:
    utility.debug_webhook.send("**DogeDenBot:** MAIN ERROR: "+str(e))
