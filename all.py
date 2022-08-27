import multiprocessing
import time

from utility import debug_webhook as debug

class BotProcess:
    def __init__(self, name: str, mainfile: str):
        self.name = name    
        self.mainfile = mainfile.replace(".py", "")

    def start(self):
        self.proc = multiprocessing.Process(target=lambda: __import__(self.mainfile))
        self.proc.start()

    def check(self):
        if not self.proc.is_alive():
            debug.send(f"**{self.name}:** Bot process is dead - restarting!")
            self.restart()

casbot = BotProcess("CASbot", "casbot.py")
doge = BotProcess("DogeDenBot", "dogedenbot.py")

debug.send("**All:** Starting all bots fresh")

casbot.start()
doge.start()

while True:
    casbot.check()
    doge.check()

    time.sleep(10)