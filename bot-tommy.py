from nextcord import *
from nextcord.ext import commands
import os
import logging
import random

TOKEN = os.getenv("DISCORD_TOKEN")

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

bot = commands.Bot(command_prefix="t?", description="Tommybot is a custom bot made for Tommylore and Sas, made by >>#0001.", owner_ids={956698441361260567,743340045628342324,901978388829450291})

logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def tommy(ctx):
    await ctx.send(random.choice(tommy_media))

@bot.command()
async def ogtommy(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/935315804067594290/947901876081422416/TOMMY.PNG")

@bot.command()
async def jinx(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/935315804067594290/947901923078586480/jinx.png")

@bot.command()
async def soggycat(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/935315804067594290/950201643578822686/soggycat.png")

@bot.command()
async def poll(ctx):
    await ctx.message.add_reaction("<:tommythumbsup:946649096645664768>")
    await ctx.message.add_reaction("<:tommythumbsdown:947042965484896287>")

@bot.command()
async def activity(ctx, *args):
    if await bot.is_owner(ctx.author):
    
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
async def tommymusic(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/935315804067594290/950854749010399334/final_621b16be7b8326006f488eb3_141970.mp4")

@bot.command()
async def dog(ctx):
    await ctx.send("https://media.discordapp.net/attachments/938385918480486421/950943566832750602/Untitled_design_6.gif")
    
@bot.command()
async def test(ctx):
    await ctx.send("goblin")
    
# add new commands before this line
bot.run(TOKEN)
