0<0# : ^
''' 
@echo off
color 0e
title Power Panel
python "%~f0" %*
pause
'''

from program import * 
import subprocess
from googlesearch import search
import json
import webbrowser
from os import system, name
from time import sleep

running = True

welcome_info = "Welcome to Power Panel - " + str(power_tools.ver)
cmd_msg(welcome_info)

while running:
	cmd_line = input(top_token)
	commands.get(cmd_line, lambda: 'Invalid')()

