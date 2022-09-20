import nextcord
from nextcord.ext import commands
import time

# Developer cog: For developer commands such as restarting the bot or changing it's custom rich presence

class Developer(commands.Cog):
    guilds = []

    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

        self.status_types = {
            "online": nextcord.Status.online, 
            "dnd": nextcord.Status.dnd, 
            "idle": nextcord.Status.idle, 
            "invisible": nextcord.Status.invisible
        }

        self.activity_types = {
            "playing": nextcord.ActivityType.playing, 
            "streaming": nextcord.ActivityType.streaming, 
            "listening to": nextcord.ActivityType.listening, 
            "watching": nextcord.ActivityType.watching, 
            "competing in": nextcord.ActivityType.competing
        }
    
    @nextcord.slash_command(description="Checks whether you are a CASbot developer or not", guild_ids=guilds)
    async def checkowner(self, interaction: nextcord.Interaction):
        if await self.bot.is_owner(interaction.user):
            await interaction.response.send_message(":white_check_mark: You are a CASbot owner!")

        else:
            await interaction.response.send_message(":x: You are not a CASbot owner.")

    @nextcord.slash_command(description="Spams a message - Dev Only", guild_ids=guilds)
    async def spam(
        self, 
        interaction: nextcord.Interaction,
        times: int = nextcord.SlashOption(name="times", description="How many times to repeat the message 1 10000", required=True),
        delay: float = nextcord.SlashOption(name="delay", description="How long to wait between each message 0 60 secs", required=True),
        content: str = nextcord.SlashOption(name="content", description="Text to send", required=True)
    ):
        if await self.bot.is_owner(interaction.user):
            print(f"CASBOT: Spamming \"{content}\" {times} times with a delay of {delay} seconds")
            await interaction.response.send_message(":white_check_mark: Sending your message(s)!")
            for i in range(times):
                await interaction.channel.send(content)
                time.sleep(delay)

        else:
            print(f"CASBOT: /spam denied user")
            await interaction.response.send_message(":x: Sorry, you do not have permission to use this command.")

    @nextcord.slash_command(description="CASbot Developer commands", guild_ids=guilds)
    async def dev(self, interaction: nextcord.Interaction):
        None

    @dev.subcommand(description="Change the bot's prescence - Dev Only")
    async def presence(
        self, 
        interaction: nextcord.Interaction,
        status_type: str = nextcord.SlashOption(name="statustype", description="Choose the status type for the bot", required=True, choices=["online", "dnd", "idle", "invisible"]),
        activity_type: str = nextcord.SlashOption(name="activitytype", description="Choose the activity type for the bot", required=True, choices=["playing", "streaming", "listening to", "watching", "competing in"]),
        activity_name: str = nextcord.SlashOption(name="activityname", description="Specify the custom activity name", required=True)
    ):
        if await self.bot.is_owner(interaction.user):
            print(f"CASBOT: Changing presence to {activity_type} {activity_name} ({status_type})")

            await self.bot.change_presence(status=self.status_types[status_type], activity=nextcord.Activity(name=activity_name, type=self.activity_types[activity_type]))
            await interaction.response.send_message(f":white_check_mark: Activity successfully set to **{activity_type} {activity_name}** ({status_type}).")

            ref = self.db.reference("/casbot/data/presence/")
            ref.child("statusType").set(status_type)
            ref.child("activityType").set(activity_type)
            ref.child("activityValue").set(activity_name)

        else:
            print(f"CASBOT: /dev presence denied user")
            await interaction.response.send_message(":x: Sorry, you do not have permission to use this command.")

    @dev.subcommand(description="Shuts down or restarts the bot - Dev Only")
    async def shutdown(self, interaction: nextcord.Interaction):
        if await self.bot.is_owner(interaction.user):
            print(f"CASBOT: RECEIVED SHUTDOWN COMMAND")
            await interaction.response.send_message(":white_check_mark: Shutting down...")
            await self.bot.close()

        else:
            print(f"CASBOT: /dev shutdown command denied user")
            await interaction.response.send_message(":x: You are not a CASbot owner.")

    @dev.subcommand(description="Makes a poll - Dev Only")
    async def poll(
        self, 
        interaction: nextcord.Interaction, 
        poll_content: str = nextcord.SlashOption(name="content", description="Poll content", required=True),
        ping_role: nextcord.Role = nextcord.SlashOption(name="role", description="Role to ping", required=False)
    ):
        if await self.bot.is_owner(interaction.user):
            print(f"CASBOT: Making poll...")

            if not ping_role:
                ping = ""
            else:
                ping = f"<@&{ping_role.id}> "

            poll_message = await interaction.channel.send(ping+poll_content)
            await poll_message.add_reaction("<:YES:976172480160997476>")
            await poll_message.add_reaction("<:NO:976172479687045141>")

            await interaction.response.send_message(":white_check_mark: Poll sent!", ephemeral=True)

        else:
            print(f"CASBOT: /poll denied user")
            await interaction.response.send_message(":x: You are not a CASbot owner.")

    @dev.subcommand(description="Sends a message via the debug webhook - Dev Only")
    async def webhook(
        self,
        interaction: nextcord.Interaction,
        message: str = nextcord.SlashOption(name="message", description="Message to send", required=True)
    ):
        if await self.bot.is_owner(interaction.user):
            print(f"CASBOT: Sent {message} through debug webhook")
            self.debug.send(f"**CASbot: {message}")
            await interaction.response.send_message(f":white_check_mark: Sent message \"{message}\" through debug webhook.")
        
        else:
            print(f"CASBOT: /dev webhook denied user")
            await interaction.response.send_message(":x: You are not a CASbot owner.")