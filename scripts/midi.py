import sys
import os
import time 
import curses 
import pygame
import pygame.midi

try:  # Ensure set available for output example
    set
except NameError:
    from sets import Set as set


class MidiOut:
    def __init__(self):
        pygame.midi.init()
        self.midi_out = pygame.midi.Output(3, 0)        
        self.midi_out.set_instrument(0)
        
    def test_midi(self, stdscr):
        # loop
        while 1:
            c = stdscr.getch()
            self.midi_out.note_on(64, 64)
            time.sleep(0.5)
            self.midi_out.note_off(64)
            if curses.keyname(c)=="q" :
                break

    def quit(self):
        del self.midi_out
        pygame.midi.quit()

    def print_device_info(self):
        pygame.midi.init()
        _print_device_info()
        pygame.midi.quit()

        def _print_device_info():
            for i in range( pygame.midi.get_count() ):
                r = pygame.midi.get_device_info(i)
                (interf, name, input, output, opened) = r

                in_out = ""
                if input:
                    in_out = "(input)"
                if output:
                    in_out = "(output)"

                print ("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
                       (i, interf, name, opened, in_out))
