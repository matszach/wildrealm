import threading


class ThreadManager:

    threads: list = []

    daemons: list = []

    @staticmethod
    def start_thread(function, args=()):
        t = threading.Thread(target=function, args=args)
        ThreadManager.threads.append(t)
        t.start()

    @staticmethod
    def start_daemon(function, args=()):
        d = threading.Thread(target=function, args=args)
        d.setDaemon(True)
        ThreadManager.daemons.append(d)
        d.start()
