import curses
import time

stdscr = curses.initscr()
# stdscr.keypad(True)
begin_x, begin_y = 20, 7
height, width = 5, 40
pad = curses.newpad(100, 100)
# These loops fill the pad with letters; addch() is
# explained in the next section
for y in range(0, 99):
    for x in range(0, 99):
        pad.addch(y, x, ord("a") + (x * x + y * y) % 26)

pad.refresh(0, 0, 5, 5, curses.LINES - 1, curses.COLS - 1)
time.sleep(10)
