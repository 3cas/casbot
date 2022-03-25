import multiprocessing

for bot in ('casbot.bot', 'tommybot.bot'):
    p = multiprocessing.Process(target=lambda: __import__(bot))
    p.start()