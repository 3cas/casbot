import multiprocessing

for bot in ('bot-cas', 'bot-tommy'):
    p = multiprocessing.Process(target=lambda: __import__(bot))
    p.start()