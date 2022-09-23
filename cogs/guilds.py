import os
with open(os.path.join("cogs", "guilds.txt"), "r") as f:
    guilds = []
    for guild_id in f.readlines():
        guilds.append(int(guild_id))