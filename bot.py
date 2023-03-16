import discord
from discord.ext import commands
import dotenv
import os
import aiohttp
import random

from cogs.misc import Miscellaneous

dotenv.load_dotenv()
TOKEN = os.getenv("CASBOT_TOKEN")
DEEPAI_KEY = os.getenv("DEEPAI_KEY")

class MyBot(commands.Bot):
    def __init__(self, *, intents: discord.Intents = discord.Intents.default()):
        super().__init__(
            intents=intents,
            command_prefix="c!",
            owner_id=743340045628342324
        )

    async def setup_hook(self) -> None:
        async for guild in self.fetch_guilds():
            print(f"Registering commands for {guild}")
            self.tree.copy_global_to(guild=guild)
        await self.tree.sync()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = MyBot(intents=intents)

# bot.add_cog(Miscellaneous(bot))

@bot.tree.command(name="hello", description="Test command which says hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello there!")

@bot.tree.command(name="fanfiction", description="Writes Konata fanfiction.")
async def fanfiction(interaction: discord.Interaction):
    await interaction.response.defer()

    url = "https://api.deepai.org/api/text-generator"
    headers = {"api-key": DEEPAI_KEY}
    data = {"text": (None, "Write some Konata Izumi fanfiction.")}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            try:
                result = (await response.json())["output"]
            except KeyError:
                result = await response.text()

    await interaction.followup.send(result)

@bot.tree.command(name="konata", description="Sends a random konata image.")
async def konata(interaction: discord.Interaction):
    page = random.randint(1, 29)
    url = f"https://konachan.net/post.json?page={page}&tags=izumi_konata"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                result = await response.json()

        for post in result:
            if post["rating"] != "s":
                result.remove(post)

        image_url = random.choice(result)["file_url"]
        await interaction.response.send_message(image_url)
    
    except Exception as e:
        await interaction.response.send_message(f"Sorry, something went wrong. Tell weirdcease#0001: `{e}`")

bot.run(TOKEN)