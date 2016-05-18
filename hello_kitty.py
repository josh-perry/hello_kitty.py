#!/usr/bin/env python

import curses
import time
import random


def setup_colors(stdscr):
	curses.start_color()
	curses.use_default_colors()

	for i in range(0, curses.COLORS):
		curses.init_pair(i + 1, i, 5)


def draw_background(stdscr):
	stdscr.bkgd(curses.color_pair(4))


kitty = """                 __                             ___            _yygL
               #####gy_,                    y#######g   __g########g
              g#F   `M##bg.                g#"'    ###g####~'    9##L
             ##F       `###g____yyyyy_____j#"        ###          ##E
            a#F           3##"#~~~~~~~#####"          ##g          ##
           j#F                           5#      ____ _##y__       ##1
           a#                           y##    _g##~####"#M##g     ##1
           #E                           J#L    ##  g#"'     `#########g_
          o#1                           ##     ## y#E         ##L     9#,
           #g                           ##      ####F         3#g      ##
          a#F                           3#L       ##L         ##M#.    ##!
         g#F                             ##_     _##g       _g#F #g   y##
        _#F                               ~###g###~M##g_   y###yg#'  y##'
        ##                                           `?"M###        g##F
       ##'                                                ?#,      ###L
       #E                                                  ##g___g#"###
      J#F                                                    `M##'   ##L
   ___##y_.      a#o                                                __##1
##""F~5#F        ###L                                 __          #M#M###M##
      J#K        ###L                                g##g             ##
     _y##ga       ~           _amog                  ####            ##F
 a###~'"#1                   d#   "#                 "##          #wy##L.
        3#,                   #g__g"                                ##""5##g
         ##g#                    ''                                a##    '~
    __y#"FH#_                                                  y_ g##
   ##"'     ##g                                                 "###g_
   ~         `9#g_                                            _g##'"9##gg,
                 ?##gy_.                                   _y##"'      `##
                     ~"####ggy_____                  ___g###F'
                             "~~~~~##################~~~" """

kitty_wink = """                 __                             ___            _yygL
               #####gy_,                    y#######g   __g########g
              g#F   `M##bg.                g#"'    ###g####~'    9##L
             ##F       `###g____yyyyy_____j#"        ###          ##E
            a#F           3##"#~~~~~~~#####"          ##g          ##
           j#F                           5#      ____ _##y__       ##1
           a#                           y##    _g##~####"#M##g     ##1
           #E                           J#L    ##  g#"'     `#########g_
          o#1                           ##     ## y#E         ##L     9#,
           #g                           ##      ####F         3#g      ##
          a#F                           3#L       ##L         ##M#.    ##!
         g#F                             ##_     _##g       _g#F #g   y##
        _#F                               ~###g###~M##g_   y###yg#'  y##'
        ##                                           `?"M###        g##F
       ##'                                                ?#,      ###L
       #E                                                  ##g___g#"###
      J#F                                                    `M##'   ##L
   ___##y_.      a#o                                                __##1
##""F~5#F        ###L                                             #M#M###M##
      J#K        ###L                                                 ##
     _y##ga       ~           _amog                  ####            ##F
 a###~'"#1                   d#   "#                              #wy##L.
        3#,                   #g__g"                                ##""5##g
         ##g#                    ''                                a##    '~
    __y#"FH#_                                                  y_ g##
   ##"'     ##g                                                 "###g_
   ~         `9#g_                                            _g##'"9##gg,
                 ?##gy_.                                   _y##"'      `##
                     ~"####ggy_____                  ___g###F'
                             "~~~~~##################~~~" """

try:
	stdscr = curses.initscr()

	curses.noecho()
	curses.cbreak()
	stdscr.keypad(1)

	setup_colors(stdscr)

	cat1 = True

	while True:
		draw_background(stdscr)

		if cat1:
			stdscr.addstr(0, 0, kitty)
			cat1 = False
		else:
			stdscr.addstr(0, 0, kitty_wink)
			cat1 = True

		stdscr.refresh()
		time.sleep(1)
finally:
	curses.nocbreak()
	stdscr.keypad(0)
	curses.echo()
	curses.endwin()
