from debug     import *
from candevice import CanDevice

import time

class Wheel(CanDevice):
    processing = True

    def __init__(self, canbus):
        debug_print_mtcall("Wheel", "__init__")
        super(Wheel, self).__init__(0, "WheelThread", canbus)
        self.canbus = canbus
        self.start()

    def run(self):
        while True:
            debug_print_mtcall("Wheel", "run1")
            if (self.processing is False):
                break
            time.sleep(1.0)

    def close(self):
        debug_print_mtcall("Wheel", "close")
        self.processing = False
        self.join()