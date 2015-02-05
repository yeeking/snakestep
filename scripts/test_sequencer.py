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

def test_sequencer(window):
    seq = sequencer.Sequencer(curses_window = window)
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

### test using normal printing
#seq = sequencer.Sequencer()
#seq.play()
#while 1:
#    pass
def keyboard_loop():
    window = curses.initscr()
    #use cbreak to not require a return key press
    curses.cbreak()
    # don't echo back the user's commands
    curses.noecho()

    while 1:
        c = window.getch()
        #seq.tick()
        window.addstr(0, 0, seq.to_string())
        if curses.keyname(c)=="q" :
            break


### test using curses
window = curses.initscr()
#use cbreak to not require a return key press
curses.cbreak()
# don't echo back the user's commands
curses.noecho()
window.keypad(1)
curses.start_color()
curses.curs_set(0)

seq = sequencer.Sequencer(curses_window = window)
seq.play()
while 1:
    c = window.getch()
    if curses.keyname(c)=="q" :
        seq.stop()
        curses.nocbreak()
        window.keypad(0)
        curses.echo()
        curses.endwin()
        #break

#while 1:
#    pass




