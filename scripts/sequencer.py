import random
import time
import thread
import clock

# Messager base class which provides basic messaging facilities        
class Messager:
#    def __init__(self):
    def send(self, message):
        x = 0
        #Print sends: "
        #print message

# define a simple class to represent a single sequence
class Sequence:
    def __init__(self, 
                 messager = Messager(), 
                 channel = 0, 
                 seq_length = 8):
        # initialise the memort
        self.memory = [[random.random()] for i in range(seq_length)]
        self.step = 0
        # how many ticks before we step?
        self.tick_per_step = 4
        self.disabled = False
        # remember how many ticks we've had
        self.tick_count = 0
        # who to send events to 
        self.messager = messager
        # when sending events, use this channel
        self.channel = channel
        # the sequence can loop over a sub sequence
        self.loop_start = 0
        # end of the sub sequence
        self.loop_end = len(self.memory) - 1
        # if we are in edit mode, we are editing this step
        self.edit_step = -1
    # call this when the clock ticks
    def tick(self):
        #print "tick"
        if self.tick_count == 0:
            #print "step"
            #print self.step
            self._play_step(self.step)
            self.step += 1
            if self.step > self.loop_end:
                self.step = self.loop_start
#            self.step = (self.step + 1) % self.play_length 
        self.tick_count = (self.tick_count + 1) % self.tick_per_step
    # read the memory at self.step and turn it into a message
    def _play_step(self, step):
        self.messager.send({"channel":self.channel, "step":self.step, "val":self.memory[step]})
    def get_memory(self):
        return self.memory
    def print_memory(self):
        print self.memory
    # describe the state of this sequence as a string
    # should probably be called to_string or something...
    def get_state_desc(self):
        state = ""
        ind = 0
        # ignore poly memory for now
        for val in self.memory:
            val = str(int(round(val[0]*9)))
            sep1 = " " 
            sep2 = " "
            # the sequence has several states for a step:
            # (ordered by priority)
            # - step is the current step -> [ ]
            if ind == self.step:
                sep1 = "-"
                sep2 = "-"
            # - step is being editod * *
            if ind == self.edit_step:
                sep1 = "*"
                sep2 = "*"
            # - step is the start of the loop -> <
            if ind == self.loop_start:
                sep1 = "["
            # - step is the end of the loop ->   >
            if ind == self.loop_end:
                sep2 = "]"
            state += sep1 + val + sep2 
            ind += 1
        return state
    # set the start of the seq loop
    def set_start(self, start):
        # assert valid start value
        if start <= self.loop_end and start < len(self.memory):
#            print "update start "+str(start)
            self.loop_start = start
            # only move the cursor if we are running earlier than the new start
            if self.step < start:
                self.step = start
    # set the end of the seq loop
    def set_end(self, end):
        # assert valid end value
        if end >= self.loop_start and end < len(self.memory):
#            print "update end "+str(end)
            self.loop_end = end
            if self.step > end:
                self.step = self.loop_start
    # enter edit mode on the sent step
    def begin_edit(self, edit_step):
        # assert valid edit_step
        if edit_step >= 0 and edit_step < len(self.memory):
            self.edit_step = edit_step
    # leave edit mode
    def end_edit(self):
        self.edit_step = -1
    # update the value of a step
    def set_edit_value(self, val):
        # assert edit mode and valid value
        if self.edit_step != -1 and val >= 0 and val <= 1:
            self.memory[self.edit_step][0] = val

# define a simple class to represent a single sequence
class Sequencer:
    def __init__(self, count=2, 
                 curses_window = None):
        # we'll write stuff here
        self.curses_window = curses_window
        self.sequences = [Sequence() for i in range(0, count)]
        self.sequences[0].set_end(5)
        self.sequences[0].begin_edit(1)
        self.sequences[0].set_edit_value(1)
        self.clock = clock.Clock()
        self.clock.add_listener(self)
# implement the 'clock listener' interface
    def tick(self):
        if self.curses_window == None:
            print (self.to_string())
        else:
            self.curses_window.addstr(0, 0, self.to_string())
            self.curses_window.refresh()
        for seq in self.sequences:
            seq.tick()

# returns a string representation of the sequencer
    def to_string(self):
        state = ""
        row = 0
        for seq in self.sequences:
            state += str(row) + ":" + seq.get_state_desc() + "\n"
            row += 1
        return state

    def play(self):
#        print "Sequencer::play"
        return self.clock.start()
        #return thread.start_new_thread(self.clock.start(), ())
    def stop(self):
        print "Sequencer::stop"

