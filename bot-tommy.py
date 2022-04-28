from nextcord import *
from nextcord.ext import commands
from nextcord.ext import tasks
from os import getenv
import logging
from random import choice

try:
    import z_private  # type: ignore
except:
    None

prefix = "t?"

WEBHOOK_URL = getenv("DEBUG_WEBHOOK")
debug = SyncWebhook.from_url(WEBHOOK_URL)

tommy_media = ["https://cdn.discordapp.com/attachments/935315804067594290/947901876081422416/TOMMY.PNG",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612810474324058/20220307_184343.jpg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612810772152341/EM7Fl_mWsAIO76k.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612811162218516/1500x500.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612811703263252/FNQ5BW_XwAYgdsd.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612811963326484/FNM5APGXsAskDXw.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612838496469002/FLDYs6ZX0AIZlmy.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612838836228106/FLlaIRlXMAQa5Jv.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612840014823454/FLzK9HCXMAcKgIx.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612840232935474/FMoa4L1XwAEbG2w.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612840505573406/FMxrD_wXsAMAqF0.jpeg",
               "https://cdn.discordapp.com/attachments/947379907959328769/950612840862076948/FMxrDffXsAUU4aS.jpeg"]

jinx_media = ["https://cdn.discordapp.com/attachments/956700543470952509/959165286542618654/oqk4nuhecnm81.png",
              "https://cdn.discordapp.com/attachments/956700543470952509/959165286823645214/gayxyciblhh81.png",
              "https://cdn.discordapp.com/attachments/956700543470952509/959165287037550622/8why8ai573b81.png",
              "https://cdn.discordapp.com/attachments/956700543470952509/959165287268220988/5f6ynu4fo2b81.png",
              "https://cdn.discordapp.com/attachments/956700543470952509/959165287670898810/unknown.png",
              "https://cdn.discordapp.com/attachments/935315804067594290/947901923078586480/jinx.png"]

gilbur_media = ["https://cdn.discordapp.com/attachments/957060354582650961/966412939571626004/gilbur.png",
                "https://cdn.discordapp.com/attachments/957060354582650961/966412939785551902/gilburgif.gif",
                "https://cdn.discordapp.com/attachments/957060354582650961/966412940137877524/gilburgif2.gif"]

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=prefix, description="Mecha Tommy is a custom bot made for Tommylore and Sas, made by >>#0001.", owner_ids={956698441361260567,743340045628342324,901978388829450291}, intents=intents)
bot.remove_command("help")

logging.basicConfig(level=logging.INFO)

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
        `{prefix}dog` - Dog
        `{prefix}poll` - Automatically reacts with <:tommythumbsup:957026236272615454> and <:tommythumbsdown:957027875977035797> for poll purposes
        `{prefix}activity` - Changes the bot prescence activity (Mods/Botmasters Only)
        `{prefix}say <text>` - Says something as tommy (Mods/Botmasters Only)
        `{prefix}test` - Sends \"goblin\""""
    help_embed = Embed(title="Mecha Tommy Commands List", description=help_desc)
    await ctx.send(embed=help_embed)

@bot.command()
async def mogu(ctx):
    await ctx.send("<:tommyfuckyou:957258224493551626>")

@bot.command()
async def tommy(ctx):
    await ctx.send(choice(tommy_media))

@bot.command()
async def gilbur(ctx):
    await ctx.send(choice(gilbur_media))

@bot.command()
async def ogtommy(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/935315804067594290/947901876081422416/TOMMY.PNG")

@bot.command()
async def jinx(ctx):
    await ctx.send(choice(jinx_media))

@bot.command()
async def soggycat(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/935315804067594290/950201643578822686/soggycat.png")

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

@bot.command()
async def tommymusic(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/935315804067594290/950854749010399334/final_621b16be7b8326006f488eb3_141970.mp4")

@bot.command()
async def dog(ctx):
    await ctx.send("https://media.discordapp.net/attachments/938385918480486421/950943566832750602/Untitled_design_6.gif")
    
@bot.command()
async def test(ctx):
    await ctx.send("goblin")

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
    
bot.run(getenv("TOMMYBOT_TOKEN"))

