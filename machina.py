#!/usr/bin/python
# -*- coding: utf-8
import curses
stdscr = curses.initscr()

from curses import wrapper


def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
curses.endwin()


"""or
chmod +x machina.py
./machina.py
"""