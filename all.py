import multiprocessing

for bot in ('casbot/bot.py', 'tommy/bot.py'):
    p = multiprocessing.Process(target=lambda: __import__(bot))
    p.start()