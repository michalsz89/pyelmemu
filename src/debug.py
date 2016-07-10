#================================== Imports ===================================#
from termcolor import cprint
from threading import Lock
#============================= Private variables ==============================#
__DEBUG_LEVEL_MASK__ = 0

__filters__ = []
lock = Lock()
#============================== Public variables ==============================#
DEBUG_LEVEL_ERR     = 1
DEBUG_LEVEL_WARN    = DEBUG_LEVEL_ERR     << 1
DEBUG_LEVEL_LOG     = DEBUG_LEVEL_WARN    << 1
DEBUG_LEVEL_FN_CALL = DEBUG_LEVEL_LOG     << 1
DEBUG_LEVEL_MT_CALL = DEBUG_LEVEL_FN_CALL << 1
DEBUG_LEVEL_ALL     = 0xFFFFFFFF
#================================== Filters ===================================#
def debug_add_filter(msg_filter):
    """Functions sets filters. If fitler is added and log msg contains a word
    defined as a filter this message will not be printed"""
    __filters__.append(msg_filter)

def __check_filter(msg):
    ret = bool()
    for f in __filters__:
        if str(f)in str(msg):
            ret = True
        else:
            ret = False
    return ret
#============================== Functions:config ==============================#
def debug_mask_set(mask):
    global __DEBUG_LEVEL_MASK__
    __DEBUG_LEVEL_MASK__ = __DEBUG_LEVEL_MASK__ | mask
#============================= Printing functions =============================#
def debug_print_log(*log):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_LOG > 0):
        msg = "[DBG]"
        for arg in log:
            if __check_filter(arg):
                return
            targ = "[%s]" % arg
            msg += targ

        cprint(msg, "blue")

def debug_print_warn(*wrn):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_WARN > 0):
        msg = "[WRN]"
        for arg in wrn:
            if __check_filter(arg):
                return
            targ = "[%s]" % arg
            msg += targ

        cprint(msg, "yellow")

def debug_print_err(*err):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_ERR > 0):
        msg = "[ERR]"
        for arg in err:
            if __check_filter(arg):
                return
            targ = "[%s]" % arg
            msg += targ

        cprint(msg, "red")

def debug_print_fncall(*foo):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_FN_CALL > 0):
        msg = "[FNC]"
        for arg in foo:
            if __check_filter(arg):
                return
            targ = "[%s]" % arg
            msg += targ

        cprint(msg, "magenta")

def debug_print_mtcall(class_name, method_name, *mt):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_MT_CALL > 0):
        msg = "[MTH][%s][%s]" % (class_name, method_name)

        if __check_filter(class_name):
            return

        if __check_filter(method_name):
            return

        for arg in mt:
            if __check_filter(arg):
                return
            targ = "[%s]" % arg
            msg += targ

        cprint(msg, "green")
