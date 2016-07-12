from debug        import *
from config       import *

from candevice    import CanDevice
from rfcommserver import RfcommServer

import time

class Elm(CanDevice):
    processing = True
    canbus = None
    dev_addr = 3

    def __init__(self, canbus):
        debug_print_mtcall("Elm", "__init__")
        super(Elm, self).__init__(5, "ElmThread", canbus)

        #rfcommserver
        self.rfcommserver = RfcommServer(6, "RfcommThread")

        self.canbus = canbus
        self.canbus.register_receiver(self)
        self.start()

    def run(self):
        while True:
            if (self.processing is False):
                break

            if (len(self.in_buffer) > 0):
                msg = self.in_buffer[self.in_buffer_cnt - 1]
                del self.in_buffer[self.in_buffer_cnt - 1]
                self.in_buffer_cnt = self.in_buffer_cnt - 1
                self.rfcommserver.send(msg)

            debug_print_mtcall("Elm", "run")
            time.sleep(elm_timeout)

    def close(self):
        debug_print_mtcall("Elm", "close")

        self.rfcommserver.close()

        self.processing = False
        self.join()
