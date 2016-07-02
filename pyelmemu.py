#from candevice import CanDevice
import time

from debug import *
from engine import Engine
from wheel  import Wheel

def initConfig():
    debug_print_fncall(initConfig.__name__)

def initEngine():
    debug_print_fncall(initEngine.__name__)
    engine = Engine()
    return engine

def initWheel():
    debug_print_fncall(initWheel.__name__)
    wheel = Wheel()
    return wheel

def initDebug():
    debug_mask_set(DEBUG_LEVEL_ALL)

def deinitEngine(engine):
    debug_print_fncall(deinitEngine.__name__)
    engine.close()

def deinitWheel(wheel):
    debug_print_fncall(deinitWheel.__name__)
    wheel.close()

if __name__ == '__main__':
    #Init
    #initConfig()
    initDebug()
    engine = initEngine()
    wheel  = initWheel()

    #Application code
    time.sleep(10)

    #Deinit
    deinitEngine(engine)
    deinitWheel(wheel)
    #deinitWhel()
