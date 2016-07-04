from debug     import *
from candevice import CanDevice

import time

class Elm(CanDevice):
    processing = True
    canbus = None

    def __init__(self, canbus):
        debug_print_mtcall("Elm", "__init__")
        super(Elm, self).__init__(5, "ElmThread", canbus)
        self.canbus = canbus
        self.start()

    def run(self):
        while True:
            if (self.processing is False):
                break

            debug_print_mtcall("Elm", "run")
            time.sleep(1.0)

    def close(self):
        debug_print_mtcall("Elm", "close")
        self.processing = False
        self.join()
