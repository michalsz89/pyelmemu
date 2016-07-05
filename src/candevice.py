import threading
from debug import *
import canbus

class CanDevice(threading.Thread):
    "TODO: add description of this class"
    in_buffer  = []
    in_buffer_size = 8
    in_buffer_cnt  = 0

    out_buffer = []
    out_buffer_size = 8
    out_buffer_cnt  = 0

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

    def notify(self, msg):
        debug_print_mtcall("CanDevice", "notify")
        debug_print_log("Class:CanDevice", msg)

        self.in_buffer.append(msg)
        self.in_buffer_cnt = self.in_buffer_cnt + 1;

        if (self.in_buffer_cnt >= self.in_buffer_size):
            del self.in_buffer[0]
            self.in_buffer_cnt = self.in_buffer_size - 1


    def send_msg(self):
        "Function set the message to can thread"
        debug_print_mtcall("CanDevice", "send_msg")
