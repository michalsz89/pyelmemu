from debug     import *
from config    import *
from candevice import CanDevice
from can       import Message

import time

class Wheel(CanDevice):
    __processing__ = True
    __canbus__     = None
    __dev_addr__   = 156

    #out buffer
    __out_buffer__ = []

    def __init__(self, canbus):
        debug_print_mtcall("Wheel", "__init__")
        super(Wheel, self).__init__(0, "WheelThread", canbus)
        self.__canbus__ = canbus
        self.__canbus__.register_receiver(self)
        self.start()

    def run(self):
        while True:
            debug_print_mtcall("Wheel", "run")
            if (self.__processing__ is False):
                break

            #get messages from canbus
            for line in self.in_buffer:
                debug_print_log("Class:Wheel", line)

            #sending data
            self.send()
            time.sleep(wheel_timeout)

    def close(self):
        debug_print_mtcall("Wheel", "close")
        self.__processing__ = False
        self.join()

    def key_press(self, key_num):
        msg = Message(timestamp = time.time(), extended_id = False, arbitration_id = self.__dev_addr__,
                data = bytearray([0, key_num]))

        str_msg = "%s" % msg

        self.out_buffer.append(str_msg)
        self.out_buffer_cnt = self.out_buffer_cnt + 1
