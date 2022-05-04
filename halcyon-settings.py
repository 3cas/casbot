from nextcord import *
from nextcord.ext import commands
from requests import get, post

import utility as u
from utility import db

try:
    import INIT_ENV  # type: ignore
except:
    None

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Change server settings", guild_ids=u.mains)
    async def set(self, interaction: Interaction):
        await interaction.response.send_message("**I LOVE LEAN!!!!**")

    @set.subcommand(description="Change how permission should be handled with the bot, either or both option(s) can be used here")
    async def permissions(
        self, 
        interaction: Interaction,
        serverperms: bool = SlashOption(name="use server perms", description="Allow users to use commands if they have permissions for that specific command", required=True),
        role: Role = SlashOption(name="role", description="Role that gives members permission to use Halcyon commands", required=False)
    ):
        if interaction.user == interaction.guild.owner:
            ref = db.reference("/halcyon/servers/"+str(interaction.guild.id)+"/settings/permissions/")
            ref.child("serverperms").set(serverperms)
            response = ":white_check_mark: Server will now use server permissions. " if serverperms else "Server will now **not** use server permissions. "

            if isinstance(role.id, int):
                ref.child("role").set(role.id)
                response += "Moderator role set to "+role.name+"."
            else:
                response += "No moderator role set."

            interaction.send(response)
        
        else:
            interaction.send(":x: Sorry, you must be server owner to change this setting.")
                    



def setup(bot):
    bot.add_cog(Test(bot))
