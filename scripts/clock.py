import time
import thread
# really basic implementation of a busy waiting clock

class Clock:
    def __init__(self):
        self.bpm(120)
        # listeners stores things that listen for clock ticks
        self._listeners = []
        # when did we last tick?
        self._last_tick = time.time()
        self._running = False

    def bpm(self, bpm):
        # 4 ticks a beat
        self._tick_length = 60.0/bpm / 4 * 1000.0

    def start(self):
        print "Clock::start"
        #thread.start_new_thread(self._run, ())
        self._run()

    def stop(self):
        print "Clock::stop"
        self._running = False

    # add something that wants to know when the clock ticks    
    def add_listener(self, listener):
        self._listeners.append(listener)

    def _run(self):
        self._running = True
        waited = self._tick_length
        while self._running:
            now = time.time()
            self._tick()
            # how long did it take to tick?
            lostms = (time.time() - now) * 0.001
            #if lostms > self._tick_length:
            #    print "Clock::tick took too long!"
            #else:
            #    self._busy_sleep(self._tick_length - lostms)
            self._busy_sleep(self._tick_length - lostms)
    def _tick(self):
	this_tick = time.time()
        print "Clock::tick diff: "+str(this_tick - self._last_tick)
        self._last_tick = this_tick 
        for listener in self._listeners:
            print "CLock::ticking a listener"
            listener.tick()
        
    def _busy_sleep(self, timems):
        timenow = time.time()
        #timed = timems / 1000.0
        timestop = time.time() + (timems * 0.001)
        timewait = (timems - 30) * 0.001
        #timewaited = 0
        if timewait > 0:
            time.sleep(timewait)
            while True:
                time.sleep(0)
                if time.time() >= timestop:
                    break;
                    #timewaited = time.time() - timenow
                    #    print "waited "+str(timewaited)
        #return timewaited

clock = Clock()
thread.start_new_thread(clock.start(), ())



while 1:
   pass
