#from candevice import CanDevice
import time

from debug import *
from engine import Engine
from wheel  import Wheel
from canbus import CanBus

def init_config():
    debug_print_fncall("initConfig")

def init_canbus():
    debug_print_fncall("initCanBus")
    return CanBus(11, "CanBusThread")

def init_engine(canbus):
    debug_print_fncall("initEngine")
    engine = Engine(canbus)
    return engine

def init_wheel(canbus):
    debug_print_fncall("initWheel")
    wheel = Wheel(canbus)
    return wheel

def init_debug():
    debug_mask_set(DEBUG_LEVEL_ALL)

def deinit_engine(engine):
    debug_print_fncall("deinitEngine")
    engine.close()

def deinit_wheel(wheel):
    debug_print_fncall("deinitWheel")
    wheel.close()

def deinit_canbus(canbus):
    debug_print_fncall("deinitCanBus")
    canbus.close()

if __name__ == '__main__':
    #Init
    #initConfig()
    init_debug()
    canbus = init_canbus()
    engine = init_engine(canbus)
    wheel  = init_wheel(canbus)

    #Application code
    time.sleep(10)

    #Deinit
    deinit_engine(engine)
    deinit_wheel(wheel)
    deinit_canbus(canbus)
    #deinitWhel()
