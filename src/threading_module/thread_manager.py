import threading


class ThreadManager:

    @staticmethod
    def start_thread(function, args=()):
        t = threading.Thread(target=function, args=args)
        t.start()

    @staticmethod
    def start_daemon(function, args=()):
        t = threading.Thread(target=function, args=args)
        t.setDaemon(True)
        t.start()
