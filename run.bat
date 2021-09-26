0<0# : ^
''' 
@echo off
color 0e
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

while running:
	cmd_line = input(top_token)
	commands.get(cmd_line, lambda: 'Invalid')()

