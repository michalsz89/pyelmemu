import threading
from debug import *

class CanDevice(threading.Thread):
    "TODO: add description of this class"
    inBuffer  = []
    outBuffer = []

    "Lock"
    lock = None

    def __init__(self, threadID, name):
        debug_print_mtcall("CanDevice", "__init__")
        self.lock = threading.Lock()

        threading.Thread.__init__(self)

        self.threadID = threadID
        self.name     = name
        self.setDaemon(True)

    def run(self):
        debug_print_mtcall("CanDevice", "run")
        self.start()
