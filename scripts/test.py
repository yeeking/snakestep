import random
import time
import thread


# Messager base class which provides basic messaging facilities        
class Messager:
#    def __init__(self):
    def send(self, message):
        print "Messager sends: "
        print message
  

# define a simple class to represent a single sequence
class Sequence:
    def __init__(self, messager = Messager(), channel = 0):
        # initialise the memort
        self.memory = [[random.random()] for i in range(32)]
        self.play_length = 8
        self.step = 0
        # how many ticks before we step?
        self.tick_per_Step = 1
        self.disabled = False
        self.tick_count = 0
        self.messager = messager
        self.channel = channel
    # call this when the clock ticks
    def tick(self):
        #print "tick"
        if self.tick_count == 0:
            #print "step"
            self.play_step(self.step)
            self.step = (self.step + 1) % self.play_length 
        self.tick_count = (self.tick_count + 1) % self.tick_per_Step
    # read the memory at self.step and turn it into a message
    def play_step(self, step):
        self.messager.send({"channel":self.channel, "step":self.step, "val":self.memory[step]})
    def get_memory(self):
        return self.memory
      
class Clock:
    def __init__(self):
        self.bpm(130)
        self.listeners = []
        self.last_tick = time.time()
        
    def start(self):
        print "Clock::start"
        thread.start_new_thread(self.run, ())

    def run(self):
        count = 0
        while count < 100:
            self.tick()
            time.sleep(self.tick_length)
            count += 1

    def stop(self):
        print "Clock::stop"

    def tick(self):
	this_tick = time.time()
        
        print "Clock::tick diff: "+str(this_tick - self.last_tick)
        self.last_tick = this_tick 
        for listener in self.listeners:
            print "ticking a listener"
            listener.tick()

    def bpm(self, bpm):
        # 4 ticks a beat
        self.tick_length = 60.0/bpm / 4
        
    # add something that wants to know when the clock ticks    
    def addListener(self, listener):
        self.listeners.append(listener)
        
        

 
    
seq = Sequence()
clock = Clock()
clock.addListener(seq)
clock.start()

while 1:
   pass
