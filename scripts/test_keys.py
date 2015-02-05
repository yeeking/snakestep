import curses
import time
import thread

# tries to write to the curses window in the background
class BackgroundWriter:
   def start(self, window, y, id):
      ind = 0
      while True:
         window.addstr(y, 0, id+":"+str(ind)+"   ")
         window.refresh()
         ind += 1
         time.sleep(1.0)


#init the curses screen
window = curses.initscr()
#use cbreak to not require a return key press
curses.cbreak()
curses.noecho()
#print "press q to quit"
quit=False
# loop
window.addstr(0, 0, "counter:")
bg1 = BackgroundWriter()
bg2 = BackgroundWriter()
t1 = thread.start_new_thread(bg1.start, (window, 1, "t1", ))
t2 = thread.start_new_thread(bg2.start, (window, 2, "t2", ))
#t.join()

while quit !=True:
   c = window.getch()
#   print "\nyou pressed "+curses.keyname(c),
   if curses.keyname(c)=="q" :
     quit=True

curses.endwin()


