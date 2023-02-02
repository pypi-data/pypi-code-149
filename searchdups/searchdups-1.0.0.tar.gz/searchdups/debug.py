import sys
from datetime import datetime

DEBUG = False

def p_debug(*args):
    if DEBUG:
        print(str(datetime.now()) + " " + " ".join([str(x) for x in args]))

def p_warning(*args):
    print(str(datetime.now()) + " " + " ".join([str(x) for x in args]))

def p_error(*args):
    print(str(datetime.now()) + " " + " ".join([str(x) for x in args]))
    sys.exit(1)

def debugLevel(debug):
    global DEBUG
    DEBUG = debug