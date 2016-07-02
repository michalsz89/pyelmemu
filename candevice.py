import threading

class CanDevice(threading):
    "TODO: add description of this class"
    inBuffer  = []
    outBuffer = []
    
    "Lock"
    lock = None

    def __init__(self):
        self.lock = threading.Lock()