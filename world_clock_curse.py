#!/usr/bin/python
import time
import curses
import curses.panel
import traceback
from worldclock import WorldClock

def main(stdscr):
  wc = WorldClock()
  curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
  
  global screen
  screen = stdscr.subwin(0, 0)

  mapWin = curses.newwin(19, 77)

  mapPanel = curses.panel.new_panel(mapWin)
  screenMaxY, screenMaxX = screen.getmaxyx()
  mapMaxY,mapMaxX = mapWin.getmaxyx()
  mapPanel.move(0,int(screenMaxX/2 - mapMaxX/2))
  mapPanel.show()

  #screen.box() # Wrap screen window in box

  while True:
    updateMap(mapWin, wc)

    screen.refresh()
    mapWin.noutrefresh()
    curses.doupdate()
    time.sleep(1)
  return



def updateMap(mapWin, wc):
    mapWin.clear()
    #screen.box()
    

    for y in range(19):
      mapWin.addstr(y, 0, wc.worldmap[y], curses.A_DIM)


    mapWin.addstr(1, 41, 'Copenhagen', curses.A_BOLD) 
    mapWin.addstr(2, 41, wc.getCopenhagenTime(), curses.A_BOLD) 

    mapWin.addstr(4, 67, 'Tokyo', curses.A_BOLD) 
    mapWin.addstr(5, 67, wc.getTokyoTime(), curses.A_BOLD)
 
    mapWin.addstr(9, 62, 'Hong Kong', curses.A_BOLD) 
    mapWin.addstr(10, 62, wc.getHongKongTime(), curses.A_BOLD)

    mapWin.addstr(5, 19, 'New York', curses.A_BOLD) 
    mapWin.addstr(6, 19, wc.getNewYorkTime(), curses.A_BOLD)

    mapWin.addstr(12, 4, 'Rarotonga', curses.A_BOLD) 
    mapWin.addstr(13, 4, wc.getRarotongaTime(), curses.A_BOLD)
 
    mapWin.addstr(11, 46, 'Nairobe', curses.A_BOLD) 
    mapWin.addstr(12, 46, wc.getNairobeTime(), curses.A_BOLD)
   
    
    #screen.refresh()
  
    

def centerTextHorizontal(screen, text):
    # Get window diminsions
    y, x = screen.getmaxyx()
    return int((x/2)-(len(text))/2)


if __name__ == '__main__':
  try:
    # Initialize curses
    stdscr=curses.initscr()

    # Turn off echoing of keys, and enter cbreak mode,
    # where no buffering is performed on keyboard input
    curses.noecho()
    curses.cbreak()

    # In keypad mode, escape sequences for special keys
    # will be interpreted and a special value like
    # curses.KEY_LEFT will be returned
    stdscr.keypad(1)
    curses.curs_set(0) # Hide cursor position

    curses.start_color()

    main(stdscr) # enter main loop
  except curses.error:
    # In the event of error, restore terminal to sane state
    traceback.print_exc() # Print the exception
    print(curses.ERR)
  except KeyboardInterrupt:
    # Caught KeyboardInterrupt (Gets rid of stacktrace)
    # Set everything back to normal before exit
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    exit()
  finally:
    # Set everything back to normal
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
