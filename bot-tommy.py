from nextcord import *
from nextcord.ext import commands
from nextcord.ext import tasks
from os import getenv
import logging
from random import randint

try:
    import INIT_ENV  # type: ignore
except:
    None

prefix = "t?"

WEBHOOK_URL = getenv("DEBUG_WEBHOOK")
debug = SyncWebhook.from_url(WEBHOOK_URL)

L_emotes = ["<:L0:970935282985742357>","<:L1:970935262316224523>","<:L2:970935250706395196>","<:L3:970935221581148170>","<:L4:970935212013912115>",
            "<:L5:970935202304106536>","<:L6:970935194255253544>","<:L7:970935185233305600>","<:L8:970935175959691314>","<:L9:970935164588933130>",
            "<:LA:970935154057039932>","<:LB:970935143315431434>","<:LC:970935133400092722>","<:LD:970935124155830292>"]

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=prefix, description="Mecha Tommy is a custom bot made for Tommylore and Plasma, made by CAS#0001.", owner_ids={956698441361260567,743340045628342324,901978388829450291}, intents=intents)
bot.remove_command("help")

logging.basicConfig(level=logging.INFO)

media_url = "https://aei.pw/media/tommylore"

def get_image(name, limit):
    return f"{media_url}/{name}/{randint(0, limit)}.png"

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    debug.send("**Mecha Tommy:** Bot has started successfully")
    refresh_member_count.start()

@bot.command()
async def help(ctx):
    help_desc = f"""`{prefix}tommy` - Sends a random tommy image
        `{prefix}ogtommy` - Sends the original tommy image
        `{prefix}tommymusic` - Sends a video of tommy with music
        `{prefix}jinx` - Sends a random image of jinx
        `{prefix}soggycat` - Sends a set image of soggy cat
        `{prefix}dog` - Sends dog
        `{prefix}gilbur` - Sends a random gilbur image
        `{prefix}poll` - Automatically reacts with <:tommythumbsup:957026236272615454> and <:tommythumbsdown:957027875977035797> for poll purposes
        `{prefix}activity` - Changes the bot prescence activity (Mods/Botmasters Only)
        `{prefix}say <text>` - Says something as tommy (Mods/Botmasters Only)
        `{prefix}ratio` - [must be reply] Ratios someone"""
    help_embed = Embed(title="Mecha Tommy Commands List", description=help_desc)
    await ctx.send(embed=help_embed)

@bot.command()
async def mogu(ctx):
    await ctx.send("<:tommyfuckyou:957258224493551626>")

@bot.command()
async def tommy(ctx):
    await ctx.send(get_image("tommy", 11))

@bot.command()
async def ogtommy(ctx):
    await ctx.send(f"{media_url}/tommy/0.png")

@bot.command()
async def gilbur(ctx):
    await ctx.send(get_image("gilbur", 2))

@bot.command()
async def jinx(ctx):
    await ctx.send(get_image("jinx", 5))

@bot.command()
async def soggycat(ctx):
    await ctx.send(f"{media_url}/misc/soggycat.png")

@bot.command()
async def tommymusic(ctx):
    await ctx.send(f"{media_url}/misc/tommymusic.mp4")

@bot.command()
async def dog(ctx):
    await ctx.send(f"{media_url}/misc/dog.gif")

@bot.command()
async def poll(ctx):
    await ctx.message.add_reaction("<:tommythumbsup:957026236272615454>")
    await ctx.message.add_reaction("<:tommythumbsdown:957027875977035797>")

@bot.command()
async def activity(ctx, *args):
    if await bot.is_owner(ctx.author) or await commands.has_role(957055780392153108):
    
        args = list(args)
        try:
            status_type = args[0]
            new_status = ' '.join(args[1:])
        except:
            await ctx.send(embed=Embed(title="Error",description=f"Not enough arguments\n\nProper command format: `t!activity <status type> <status>`\nStatus type: `playing`, `streaming`, `listening`, `watching`", color=0xff0000))
        else:
            if len(args) > 1:
                if status_type == "playing":
                    await bot.change_presence(activity=Game(name=new_status))
                    await ctx.send(embed=Embed(title="Success",description=f"Activity successfully changed to \"Playing {new_status}\".", color=0x00ff00))
                elif status_type == "streaming":
                    await bot.change_presence(activity=Streaming(name=new_status, url="https://google.com"))
                    await ctx.send(embed=Embed(title="Success",description=f"Activity successfully changed to \"Streaming {new_status}\".", color=0x00ff00))
                elif status_type == "listening":
                    await bot.change_presence(activity=Activity(type=ActivityType.listening, name=new_status))
                    await ctx.send(embed=Embed(title="Success",description=f"Activity successfully changed to \"Listening to {new_status}\".", color=0x00ff00))
                elif status_type == "watching":
                    await bot.change_presence(activity=Activity(type=ActivityType.watching, name=new_status))
                    await ctx.send(embed=Embed(title="Success",description=f"Activity successfully changed to \"Watching {new_status}\".", color=0x00ff00))
                else:
                    await ctx.send(embed=Embed(title="Error",description=f"Improper arguments\n\nProper command format: `t!activity <status type> <status>`\nStatus type: `playing`, `streaming`, `listening`, `watching`", color=0xff0000))
            else:
                await ctx.send(embed=Embed(title="Error",description=f"Not enough arguments\n\nProper command format: `t!activity <status type> <status>`\nStatus type: `playing`, `streaming`, `listening`, `watching`", color=0xff0000))

    else:
        await ctx.send("lol no")

@bot.command()
async def say(ctx, *, text: str):
    if await bot.is_owner(ctx.author) or await commands.has_role(957055780392153108):
        try:
            await ctx.message.delete()
        except:
            None
        await ctx.send(text)
    else:
        await ctx.send("lol no")

count_guilds = {957025882399195156: 968177603880058910}

@tasks.loop(seconds=10.0)
async def refresh_member_count():
    try:
        for guild_id in count_guilds:
            guild = bot.get_guild(guild_id) # tommylore
            channel = guild.get_channel(count_guilds[guild_id])
            await channel.edit(name="Members: "+str(len(guild.humans)))
    except:
        None
    
@bot.command()
async def ratio(ctx):
    try:
        Lmsg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    except:
        await ctx.send("you didn't reply to anyone lol")
    else:
        for emote in L_emotes:
            await Lmsg.add_reaction(emote)
        

bot.run(getenv("TOMMYBOT_TOKEN"))

