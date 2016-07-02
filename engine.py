from debug     import *
from candevice import CanDevice

import time

class Engine(CanDevice):
    processing = True

    def __init__(self):
        debug_print_mtcall("Engine", "__init__")
        super(Engine, self).__init__(0, "EngineThread")
        self.start()

    def run(self):
        debug_print_mtcall("Engine", "run1")
        while True:
            debug_print_mtcall("Engine", "run2")
            if (self.processing is False):
                debug_print_mtcall("Engine", "run3")
                break

            time.sleep(1.0)

    def close(self):
        debug_print_mtcall("Engine", "close")
        self.processing = False
        self.join()
