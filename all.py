from multiprocessing import Process
from time import sleep
from nextcord import SyncWebhook
from os import getenv

try:
    import z_private
except:
    None

WEBHOOK_URL = getenv("DEBUG_WEBHOOK")
debug = SyncWebhook.from_url(WEBHOOK_URL)

casbot = Process(target=lambda: __import__("bot-cas"))
tommybot = Process(target=lambda: __import__("bot-tommy"))

debug.send("**All:** Starting all bots fresh")
casbot.start()
tommybot.start()

while True:
    if not casbot.is_alive():
        debug.send("**CASbot:** Bot process is dead - restarting!")
        casbot = Process(target=lambda: __import__("bot-cas"))
        casbot.start()

    if not tommybot.is_alive():
        debug.send("**Mecha Tommy:** Bot process is dead - restarting!")
        tommybot = Process(target=lambda: __import__("bot-tommy"))
        tommybot.start()
    
    sleep(10)
