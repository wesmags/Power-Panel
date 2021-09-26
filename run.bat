0<0# : ^
''' 
@echo off
color 0e
python "%~f0" %*
pause
'''

top_token = ":"
sub_token_1 = "-" + top_token
sub_token_2 = " $" + top_token

from program import * 
import subprocess
from googlesearch import search
import json
import webbrowser

from os import system, name
from time import sleep
  


power_tools = Program("Windows Power Tools", 0.1)




running = False
sandbox = True

py_docs = "https://docs.python.org/3/"

while running:
    cmd_line = input(top_token)
    if cmd_line == "program":
        pro_sub = input(sub_token_1)
        if pro_sub == "info":
            power_tools.log_info()
    if cmd_line == "help":
        for cmd in help:
            print("Available Commands: ")
            print(cmd)
    if cmd_line == "cls":
        clear()
    if cmd_line == "google":
        google_sub = input(sub_token_1)
        if google_sub == "results":
            results = input(sub_token_2)
            for res in search(results, tld="co.in", num=10, stop=10, pause=2):
                print(sub_token_2 + res)
    if cmd_line == "docs":
        docs_sub = input(sub_token_1)
        if docs_sub == "python":
            webbrowser.open(py_docs);

        
    #else:
    #    print("Error: Command Not Recognized")
    
while sandbox:
	cmd_line = input(top_token)
	commands[cmd_line]()

