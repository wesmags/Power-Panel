0<0# : ^
''' 
@echo off
color 1a
python "%~f0" %*
'''

from program import * 
import subprocess


power_tools = Program("Windows Power Tools", 0.1)

debug_commands = []

help = ['program'] 

while True:
    cmd_line = input(":")
    if cmd_line == "test":
        print("test success")
    if cmd_line == "program":
        pro_sub = input("-:")
        if pro_sub == "info":
            power_tools.log_info()
    if cmd_line == "help":
        for cmd in help:
            print(cmd)
    if cmd_line == "cls":
        pass
