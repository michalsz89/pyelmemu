#"File get debug level from the config and print valid info."
#"TODO: Use colors"
#"TOOD: Add logging to file ability"

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

def debug_print_log(msg):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_LOG > 0):
        print "[DBG][%s]" % (msg)

def debug_print_warn(msg):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_WARN > 0):
        print "[WRN][%s]" % (msg)

def debug_print_err(msg):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_ERR > 0):
        print "[ERR][%s]" % (msg)

def debug_print_fncall(msg):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_FN_CALL > 0):
        print "[FNC][%s]" % (msg)

def debug_print_mtcall(class_name, method_name):
    if (__DEBUG_LEVEL_MASK__ & DEBUG_LEVEL_MT_CALL > 0):
        print "[MTH][%s][%s]" % (class_name, method_name)
