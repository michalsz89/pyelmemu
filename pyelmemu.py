#from candevice import CanDevice
from debug import *
 
def initConfig():
    debug_print_fncall(initConfig.__name__)

def initEngine():
    debug_print_fncall(initEngine.__name__)

def initWheel():
    debug_print_fncall(initWheel.__name__)

def initDebug():
    debug_mask_set(DEBUG_LEVEL_ERR)
    debug_mask_set(DEBUG_LEVEL_FN_CALL)

if __name__ == '__main__':
    initConfig()
    initDebug()
    #initCan()
    initEngine()
    initWheel()
    #initElm()

    