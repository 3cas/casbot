from multiprocessing import Process
from time import sleep
from utility import debug_webhook as debug

class BotProcess:
    def __init__(self, name: str, mainfile: str):
        self.name = name    
        self.mainfile = mainfile.replace(".py", "")

    def start(self):
        self.proc = Process(target=lambda: __import__(self.mainfile))
        self.proc.start()

    def check(self):
        if not self.proc.is_alive():
            debug.send(f"**{self.name}:** Bot process is dead - restarting!")
            self.restart()

casbot = BotProcess("CASbot", "bot-cas.py")
mechatommy = BotProcess("Mecha Tommy", "bot-tommy.py")
halcyon = BotProcess("Halcyon", "bot-halcyon.py")

debug.send("**All:** Starting all bots fresh")

casbot.start()
mechatommy.start()

while True:
    casbot.check()
    mechatommy.check()

    sleep(10)