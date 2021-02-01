import curses

def window(stdscr):

  (sh, sw) = stdscr.getmaxyx()

  # print the welcome message
  stdscr.addstr(sh //2, sw //2, "hello curses!")

  # wait user's input before finish
  stdscr.getch()

curses.wrapper(window)