from debug     import *
from config    import *
from candevice import CanDevice

import time

class Elm(CanDevice):
    processing = True
    canbus = None
    dev_addr = 3

    def __init__(self, canbus):
        debug_print_mtcall("Elm", "__init__")
        super(Elm, self).__init__(5, "ElmThread", canbus)
        self.canbus = canbus
        self.canbus.register_receiver(self)
        self.start()

    def run(self):
        while True:
            if (self.processing is False):
                break

            for line in self.in_buffer:
                debug_print_log("ELM", line)

            debug_print_mtcall("Elm", "run")
            time.sleep(elm_timeout)

    def close(self):
        debug_print_mtcall("Elm", "close")
        self.processing = False
        self.join()
