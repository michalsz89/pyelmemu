from termcolor import cprint

__DEBUG_LEVEL_MASK__ = 0

DEBUG_LEVEL_ERR     = 1
DEBUG_LEVEL_WARN    = DEBUG_LEVEL_ERR     << 1
DEBUG_LEVEL_LOG     = DEBUG_LEVEL_WARN    << 1
DEBUG_LEVEL_FN_CALL = DEBUG_LEVEL_LOG     << 1
DEBUG_LEVEL_MT_CALL = DEBUG_LEVEL_FN_CALL << 1
DEBUG_LEVEL_ALL     = 0xFFFFFFFF

def debug_mask_set(mask):
    global __DEBUG_LEVEL_MASK__
    __DEBUG_LEVEL_MASK__ = __DEBUG_LEVEL_MASK__ | mask

def debug_print_log(log):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_LOG > 0):
        msg = "[DBG][%s]" % (log)
        cprint(msg, "grey")

def debug_print_warn(wrn):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_WARN > 0):
        msg = "[WRN][%s]" % (wrn)
        cprint(msg, "yellow")

def debug_print_err(err):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_ERR > 0):
        msg = "[ERR][%s]" % (err)
        cprint(msg, "red")

def debug_print_fncall(foo_name):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_FN_CALL > 0):
        msg = "[FNC][%s]" % (foo_name)
        cprint(msg, "magenta")

def debug_print_mtcall(class_name, method_name):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_MT_CALL > 0):
        msg = "[MTH][%s][%s]" % (class_name, method_name)
        cprint(msg, "green")
