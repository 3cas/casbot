from nextcord import *
from nextcord.ext import commands
import logging
from os import getenv
import time

import cb_ext.util as u
from cb_ext.owner import Owner
from cb_ext.test import Test
from cb_ext.misc import Misc

bot = commands.Bot(command_prefix="c!", description="CASbot is a test bot created by CAS, aka >>#0001.", owner_ids=u.owners)

logging.basicConfig(level=logging.INFO)

bot.add_cog(Owner(bot))
bot.add_cog(Test(bot))
bot.add_cog(Misc(bot))

WEBHOOK_URL = getenv("DEBUG_WEBHOOK")
debug = Webhook.from_url(WEBHOOK_URL)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await debug.send("**CASbot:** Bot has started successfully")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('c!hello'):
        await message.channel.send('Hello!')

try:
    import z_private
except:
    None

TOKEN = getenv("CASBOT_TOKEN")

while True:
    bot.run(TOKEN)
    time.sleep(1)