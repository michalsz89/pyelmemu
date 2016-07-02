#from candevice import CanDevice
from debug import *
from engine import Engine
import time


def initConfig():
    debug_print_fncall(initConfig.__name__)

def initEngine():
    debug_print_fncall(initEngine.__name__)
    engine = Engine()
    return engine

def initWheel():
    debug_print_fncall(initWheel.__name__)

def initDebug():
    debug_mask_set(DEBUG_LEVEL_ALL)

def deinitEngine(engine):
    debug_print_fncall(deinitEngine.__name__)
    engine.close()

def deinitWhel():
    debug_print_fncall(deinitWhel.__name__)

if __name__ == '__main__':
    #Init
    #initConfig()
    initDebug()
    engine = initEngine()
    #initWheel()

    #Application code
    time.sleep(10)

    #Deinit
    deinitEngine(engine)
    #deinitWhel()
