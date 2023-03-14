import discord
from discord.ext import commands
import dotenv
import os
import aiohttp

dotenv.load_dotenv()
TOKEN = os.getenv("CASBOT_TOKEN")
DEEPAI_KEY = os.getenv("DEEPAI_KEY")

class MyBot(commands.Bot):
    def __init__(self, *, intents: discord.Intents = discord.Intents.default()):
        super().__init__(intents=intents, command_prefix="c!")

    async def setup_hook(self) -> None:
        async for guild in self.fetch_guilds():
            print(f"Registering commands for {guild}")
            self.tree.copy_global_to(guild=guild)
        await self.tree.sync()

bot = MyBot()

@bot.tree.command(name="hello", description="Test command which says hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello there!")

@bot.tree.command(name="fanfiction", description="Writes Walter Clements fanfiction.")
async def fanfiction(interaction: discord.Interaction):
    await interaction.response.defer()

    url = "https://api.deepai.org/api/text-generator", 
    headers = {"api-key": DEEPAI_KEY}
    data = {"text": (None, "my name is Walter Clements. i like fire trucks and moster trucks.")}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            try:
                result = response.json()["output"]
            except KeyError:
                result = response.text

    await interaction.followup.send(result)

bot.run(TOKEN)