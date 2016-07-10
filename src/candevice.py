import threading
import canbus

from debug import *

class CanDevice(threading.Thread):
    "Lock"
    lock = None

    "Handle to can bus object. It cannot be a copy! canBus will be a singleton"
    canbus = None

    def __init__(self, threadID, name, canbus):
        debug_print_mtcall("CanDevice", "__init__")
        self.lock = threading.Lock()

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name     = name
        self.canbus   = canbus
        self.setDaemon(True)

        #input buffer of a device
        self.in_buffer = []
        self.in_buffer_size = 8
        self.in_buffer_cnt  = 0

        #output buffer
        self.out_buffer = []
        self.out_buffer_size = 8
        self.out_buffer_cnt  = 0

    def notify(self, msg):
        debug_print_mtcall("CanDevice", "notify")
        self.in_buffer.append(msg)
        self.in_buffer_cnt = self.in_buffer_cnt + 1;

        if (self.in_buffer_cnt >= self.in_buffer_size):
            del self.in_buffer[0]
            self.in_buffer_cnt = self.in_buffer_size - 1

    def send(self):
        debug_print_mtcall("CanDevice", "send")
        lock.acquire(True)
        size = len(self.out_buffer)
        if (len(self.out_buffer) > 0):
            msg = self.out_buffer[self.out_buffer_cnt - 1]
            self.canbus.put_msg(msg)
            del self.out_buffer[self.out_buffer_cnt - 1]
            self.out_buffer_cnt = self.out_buffer_cnt - 1
        lock.release()
