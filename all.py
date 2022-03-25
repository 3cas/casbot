import multiprocessing

for bot in ('casbot.bot', 'tommy.bot'):
    p = multiprocessing.Process(target=lambda: __import__(bot))
    p.start()