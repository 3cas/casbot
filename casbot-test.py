import nextcord

import utility

# Test cog: For future reference and testing things with Nextcord
# NOTE: This cog is not loaded

class Test(nextcord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=utility.mains)  # Making the command and limiting the guilds
    async def test(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("Tested")

    @test.subcommand(description="Test subcommand")  # Identifying The Sub-Command
    async def subcommand_one(self, interaction: nextcord.Interaction):  # Making The Sub Command Name And Passing Through Interaction
        await interaction.response.send_message("This is subcommand 1!")  # Sending A Response

    # Identifying The Sub-Command And Adding A Descripton
    @test.subcommand()
    async def subcommand_two(self, interaction: nextcord.Interaction):  # Passing in interaction
        await interaction.response.send_message("This is subcommand 2!")  # Responding with a message

    @test.subcommand(description="Test menu")
    async def choose_a_number(
        self,
        interaction: nextcord.Interaction,
        number: str = nextcord.SlashOption(name="settings", description="Configure Your Settings", choices={"1": "one", "2": "two","3": "three"})):
            await interaction.response.send_message(f"You chose {number}")

    """
    @user_command()
    async def hello(self, interaction: Interaction, member: Member):
        await interaction.response.send_message(f"Hello! {member}")

    @message_command()
    async def say(self, interaction: Interaction, message: Message):
        await interaction.response.send_message(message.content, ephemeral=True)
    """

def setup(bot):
    bot.add_cog(Test(bot))