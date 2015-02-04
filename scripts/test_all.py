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
#    c = sys.stdin.read(1)
#    while c != 'q':
#        c = sys.stdin.read(1)
#        pass

def proc_key_in():
    c = sys.stdin.read(1)
    while c != 'q':
        c = sys.stdin.read(2)
        print "\n\nyou typed: "+c
#        pass


#thread.start_new_thread(proc_key_in(), ())
stdscr = curses.initscr()
#use cbreak to not require a return key press
curses.cbreak()
curses.noecho()

#test_sequencer()

print "hello"

while 1:
    c = stdscr.getch()
    if curses.keyname(c)=="q" :
        break
        curses.endwin()



