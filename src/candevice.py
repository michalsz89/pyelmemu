import threading
from debug import *
import canbus

class CanDevice(threading.Thread):
    "TODO: add description of this class"
    inBuffer  = []
    outBuffer = []

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

    def get_msg(self):
        "Function get the message from the can thread"
        debug_print_mtcall("CanDevice", "get_msg")

    def send_msg(self):
        "Function set the message to can thread"
        debug_print_mtcall("CanDevice", "send_msg")
