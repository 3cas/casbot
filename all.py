from multiprocessing import Process
from time import sleep

casbot = Process(target=lambda: __import__("bot-cas"))
tommybot = Process(target=lambda: __import__("bot-tommy"))

casbot.start()
tommybot.start()

while True:
    if not casbot.is_alive():
        casbot = Process(target=lambda: __import__("bot-cas"))
        casbot.start()
        
    if not tommybot.is_alive():
        tommybot = Process(target=lambda: __import__("bot-tommy"))
        tommybot.start()
    
    sleep(10)
