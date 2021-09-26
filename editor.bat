0<0# : ^
''' 
@echo off
color 0e
title Power Panel (Editor)
python "%~f0" %*
'''


import curses
import subprocess

menu = ['Open', 'New', 'Read', 'Exit']


def print_menu(stdscr, selected_row_idx):
	stdscr.clear()
	h, w = stdscr.getmaxyx()
	for idx, row in enumerate(menu):
		x = w//2 - len(row)//2
		y = h//2 - len(menu)//2 + idx
		if idx == selected_row_idx:
			stdscr.attron(curses.color_pair(1))
			stdscr.addstr(y, x, row)
			stdscr.attroff(curses.color_pair(1))
		else:
			stdscr.addstr(y, x, row)
	stdscr.refresh()


def print_center(stdscr, text):
	stdscr.clear()
	h, w = stdscr.getmaxyx()
	x = w//2 - len(text)//2
	y = h//2
	stdscr.addstr(y, x, text)
	stdscr.refresh()


def main(stdscr):
	# turn off cursor blinking
	curses.curs_set(0)
	# curses.curs_set(0) in editor
	

	# color scheme for selected row
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

	# specify the current selected row
	current_row = 0

	# print the menu
	print_menu(stdscr, current_row)

	while 1:
		key = stdscr.getch()

		if key == curses.KEY_UP and current_row > 0:
			current_row -= 1
		elif key == curses.KEY_DOWN and current_row < len(menu)-1:
			current_row += 1
		elif key == curses.KEY_ENTER or key in [10, 13]:
			if current_row == 3:
				stdscr.clear()
				workdr = r"C:\Users\Wes Mags\Documents\Projects\Power Tools" + r"\run.bat"
				subprocess.call(workdr)
			print_center(stdscr, "You selected '{}'".format(menu[current_row]))
			stdscr.getch()
			
			
				

		print_menu(stdscr, current_row)


curses.wrapper(main)
