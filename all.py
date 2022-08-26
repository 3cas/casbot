from multiprocessing import Process
from time import sleep
from nextcord import SyncWebhook
from os import getenv

try:
    import INIT_ENV
except:
    None

WEBHOOK_URL = getenv("DEBUG_WEBHOOK")
debug = SyncWebhook.from_url(WEBHOOK_URL)

casbot = Process(target=lambda: __import__("casbot"))
dogedenbot = Process(target=lambda: __import__("dogedenbot"))

debug.send("**All:** Starting all bots fresh")
casbot.start()
dogedenbot.start()

while True:
    if not casbot.is_alive():
        debug.send("**CASbot:** Bot process is dead - restarting!")
        casbot = Process(target=lambda: __import__("casbot"))
        casbot.start()

    if not dogedenbot.is_alive():
        debug.send("**DogeDenBot:** Bot process is dead - restarting!")
        dogedenbot = Process(target=lambda: __import__("dogedenbot"))
        dogedenbot.start()
    
    sleep(10)