from debug     import *
from config    import *
from candevice import CanDevice

import time

class Engine(CanDevice):
    processing = True
    canbus     = None
    dev_addr   = 1

    #private data
    __rpm__  = 800
    __temp__ = 90.0
    __bost__ = 0.0

    def __init__(self, canbus):
        debug_print_mtcall("Engine", "__init__")
        super(Engine, self).__init__(0, "EngineThread", canbus)
        self.canbus = canbus
        self.canbus.register_receiver(self)
        self.start()

    def run(self):
        while True:
            if (self.processing is False):
                break

            time.sleep(engine_timeout)

    def close(self):
        debug_print_mtcall("Engine", "close")
        self.processing = False
        self.join()
