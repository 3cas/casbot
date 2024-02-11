import discord
from discord.ext import commands
import random
import sqlite3
from datetime import datetime
from datetime import timedelta
import os

from migrator import dumb_migrate_db
import econlore as lore

DB_NAME = "econ.db"

with open("econ_schema.sql", "r") as f:
    econ_schema = f.read()

if os.path.isfile(DB_NAME):
    con = sqlite3.connect(DB_NAME)
    dumb_migrate_db(con, econ_schema, allow_deletions=True)
else:
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.executescript(econ_schema)
    con.commit()
    con.close()

def now():
    return datetime.timestamp(datetime.now())

starter_items = ["hamburger", "alcohol", "slot_token", "blueberries", "cheese", "cookie", "thc_cart"]

class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.con = sqlite3.connect(DB_NAME)
        self.cur = con.cursor()

    async def initiate(self, inter: discord.Interaction):
        disc_id = inter.user.id

        init_bank = random.randint(400, 1000)
        init_wallet = random.randint(10, 60)

        init_items = []
        for _ in range(random.randint(3, 5)):
            init_items.append(random.choice(starter_items))

        for item in init_items:
            self.cur.execute(
                "INSERT INTO items(type, ctime, owner) VALUES(?, ?, ?)",
                (item, now(), disc_id)
            )

        self.cur.execute(
            "INSERT INTO users(did, rtime, bank, wallet) VALUES (?, ?, ?, ?);",
            (disc_id, now(), init_bank, init_wallet),
        )

        inter.response.send_message(f":wave: Hi, and welcome to the CASbot Economy! You have just run your first economy command, and have been registered in the system.\n- Received **${init_bank}** in your bank and **${init_wallet}** in your wallet.\n- You also received **{len(init_items)} random items**, which you can check out with **/inventory**.")

    async def user_check(self, inter: discord.Interaction):
        disc_id = inter.user.id
        ban = self.cur.execute("SELECT time, until, reason FROM bans WHERE user = ? AND until < ?;", (disc_id, now())).fetchone()
        if ban:
            await inter.response.send_message(f":warning: **You have been banned** from the economy system.\nBanned at: {datetime.strftime(ban[0], '%d %B %Y at %I:%M')}\n- Reason: {ban[2]}\n- Until: {datetime.strftime(ban[1], '%d %B %Y at %I:%M')}\n\nYou will not be able to access the service while banned. You can appeal this ban by contacting Discord user @dogocean1.", ephemeral=True)

        bal = self.cur.execute("SELECT balance FROM users WHERE did = ?", (disc_id,)).fetchone()
        if not bal:
            await self.initiate(inter)

    @commands.command(description="Retrieve your daily payment.")
    async def daily(self, inter: discord.Interaction):
        await self.user_check(inter)
        payout = random.randint(50, 300)
        self.cur.execute(f"UPDATE users SET wallet = wallet + {payout} WHERE did = ?;", (inter.user.id,))
        self.cur.execute("INSERT INTO cooldowns(start, until, name) VALUES(?, ?, ?);", (now(), now()+timedelta(hours=24), "daily"))
        await inter.response.send_message(f":money_mouth: Paid you **${payout}** to your wallet!")

    @commands.command(description="Deposit money into your bank account, to keep it safe from thieves,")
    async def deposit(self, inter: discord.Interaction):
        await self.user_check(inter)
        did = inter.user.id
        self.cur.execute("UPDATE users SET bank = bank + wallet, wallet = 0 WHERE did = ?", (did,))
        await inter.response.send_message(f":arrow_right::pig: Deposited all your money into the bank.")

    @commands.command(description="Withdraw money from your bank account.")
    async def withdraw(self, inter: discord.Interaction):
        pass

    @commands.command(description="View the contents of the inventory, as well as the bank and wallet levels.")
    async def inventory(self, inter: discord.Interaction):
        await self.user_check(inter)
        did = inter.user.id
        items = self.cur.execute("SELECT type FROM items WHERE owner = ?;", (did,)).fetchall()
        bank, wallet = self.cur.execute("SELECT bank, wallet FROM users WHERE did = ?;", (did,)).fetchone()
        
        items_dict = {}
        for item in items:
            if item in items_dict:
                items_dict[item] += 1
            else:
                items_dict[item] = 1

        await inter.response.send_message(f"You have **${bank}** in the bank, **${wallet}** in your wallet, and the following items:\n{'Nn'.join(['- '+items_dict[item]+'x '+item for item in items]).replace('Nn','\n')}")