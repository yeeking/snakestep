import midi
import pygame
# this enables event capture
#pygame.init()
import curses
# init the curses screen
screen = curses.initscr()
#use cbreak to not require a return key press
curses.cbreak()
curses.noecho()
screen.addstr("any key to play a note, q to quit")
mout = midi.MidiOut()
mout.test_midi(screen)
mout.quit()
curses.endwin()
