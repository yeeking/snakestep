import random
import time
import thread
import sys

# this enables event capture
#pygame.init()
import curses

import pygame
# my custom stuff
import clock 
import sequencer
import midi

def test_sequencer():
    seq = sequencer.Sequencer()
    seq.play()

def test_sequence():
    seq = sequencer.Sequence()
    seq.print_memory()
    seq.set_start(2)
    seq.set_end(2)
    for i in range(5):
        seq.tick()

def test_clock():
    cl = clock.Clock()
    thread.start_new_thread(cl.start(), ())

test_sequencer()

while 1:
    pass




