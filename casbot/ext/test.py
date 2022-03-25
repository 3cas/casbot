from nextcord import *
from nextcord.ext import commands

import ext.util as u

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=u.mains)  # Making the command and limiting the guilds
    async def test(self, interaction: Interaction):
        await interaction.response.send_message("Tested")

    @test.subcommand(description="Test subcommand")  # Identifying The Sub-Command
    async def subcommand_one(self, interaction: Interaction):  # Making The Sub Command Name And Passing Through Interaction
        await interaction.response.send_message("This is subcommand 1!")  # Sending A Response

    # Identifying The Sub-Command And Adding A Descripton
    @test.subcommand()
    async def subcommand_two(self, interaction: Interaction):  # Passing in interaction
        await interaction.response.send_message("This is subcommand 2!")  # Responding with a message

    @test.subcommand(description="Test menu")
    async def choose_a_number(
        self,
        interaction: Interaction,
        number: str = SlashOption(name="settings", description="Configure Your Settings", choices={"1": "one", "2": "two","3": "three"})):
            await interaction.response.send_message(f"You chose {number}")

    """
    @user_command()
    async def hello(self, interaction: Interaction, member: Member):
        await interaction.response.send_message(f"Hello! {member}")

    @message_command()
    async def say(self, interaction: Interaction, message: Message):
        await interaction.response.send_message(message.content, ephemeral=True)
    """