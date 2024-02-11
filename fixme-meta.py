import discord
from discord.ext import commands

# Meta cog: For information about the bot's uptime, latency, and Libre board temperature

class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(description="Gets latency of the bot")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"My latency is `{self.bot.latency}ms.`")
        
    @discord.slash_command(description="Gets temperature of the bot's host device")
    async def temperature(self, interaction: discord.Interaction):
        try:
            with open("/sys/class/hwmon/hwmon0/temp1_input", "r") as f:
                temperature = f.read()
            
            celsius = float(temperature[:2])
            fahrenheit = (celsius * 1.8) + 32

            await interaction.response.send_message(f"Board temperature is {celsius}\u00b0C ({fahrenheit}\u00b0F).")
        
        except FileNotFoundError:
            await interaction.response.send_message("This bot is not running on Le Potato!")