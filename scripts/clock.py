import time

def busy_sleep(timems):
    timenow = time.time()
    timed = timems / 1000.0
    timestop = timenow + timed
    timewait = (timems - 20)/ 1000.0
#    print timenow
#    print timed
#    print timestop
#    print timewait
    time.sleep(timewait)
    while True:
        time.sleep(0)
        if time.time() >= timestop:
            break;
    timewaited = time.time() - timenow
    return timewaited

busy_sleep(100)

    
