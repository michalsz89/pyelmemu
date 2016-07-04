import threading
import time

from debug import *

class CanBus(threading.Thread):
    #All msg storage
    __buffer__ = []

    #Buffer size
    __buffer_size__  = 8
    __current_size__ = 0

    lock = None

    #End flag
    processing = True

    def __init__(self, threadID, name):
        debug_print_mtcall("CanBus", "__init__")

        self.lock = threading.Lock()
        threading.Thread.__init__(self)

        self.threadID = threadID
        self.name     = name
        self.setDaemon(True)
        self.start()

    def run(self):
        while True:
            if (self.processing is False):
                break

            debug_print_mtcall("CanBus", "run")
            time.sleep(1.0)

    def close(self):
        debug_print_mtcall("CanBus", "close")
        self.processing = False
        self.join()

    def put_msg(self, msg):
        debug_print_mtcall("CanBus", "put_msg")
        self.lock.acquire(True)
        self.__buffer__.append(msg)
        debug_print_log(msg)
        dbg_msg2 = "buffer size %d" % (len(self.__buffer__))
        debug_print_log(dbg_msg2)
        self.__current_size__ = self.__current_size__ + 1
        if (self.__current_size__ >= self.__buffer_size__):
            del self.__buffer__[0]

        self.lock.release()

    def get_msg(self,msg):
        self.lock.acquire(True)
        msg = self.__buffer__[self.__current_size__ - 1]
        self.lock.release()
        return msg

    def dump_buffer(self):
        debug_print_mtcall("CanBus", "dump_buffer")
        self.lock.acquire(True)
        for line in self.__buffer__:
            debug_print_log(line)
        self.lock.release()
