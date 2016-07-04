from debug     import *
from candevice import CanDevice

import time

class Engine(CanDevice):
    processing = True
    canbus = None

    def __init__(self, canbus):
        debug_print_mtcall("Engine", "__init__")
        super(Engine, self).__init__(0, "EngineThread", canbus)
        self.canbus = canbus
        self.rpm = "1200"
        self.start()

    def run(self):
        while True:
            if (self.processing is False):
                break

            self.canbus.put_msg(self.rpm)
            debug_print_mtcall("Engine", "run")
            time.sleep(0.1)

    def close(self):
        debug_print_mtcall("Engine", "close")
        self.processing = False
        self.join()
