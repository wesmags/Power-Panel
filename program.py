import subprocess
from googlesearch import search
import json
import webbrowser

from os import system, name
from time import sleep


top_token = ":"
sub_token_1 = "-" + top_token
sub_token_2 = " $" + top_token


class Program:
    def __init__(self, title, ver):
        self.title = title
        self.ver = ver
    def check(self, e_check):
        self.e_check = e_check
        print(self.e_check)
    def log_info(self):
        print("Project Title: " + self.title)
        print("Program Version: " + str(self.ver))
        


power_tools = Program("Windows Power Panel", 0.1)

def check_input(_dict, _input):
    _dict[_input]()

def test():
    print("test")
    
def help():
	for accessor, func, in commands.items():
		print(accessor, '->', func)

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def program():
    pro_sub = input(sub_token_1)
    program_commands[pro_sub]()


def info():
    power_tools.log_info()
    
def docs():
    docs_sub = input(sub_token_1)
    webbrowser.open(docs_query[docs_sub]);
    
def google():
    google_sub = input(sub_token_1)
    google_commands[google_sub]()

def results():
    results = input(sub_token_2)
    for res in search(results, tld="co.in", num=10, stop=10, pause=2):
                print(sub_token_2 + res)


commands = {
    # Dict full of accessers for comamnds - command : "command_call"
    'help' : help,
	'test' : test,
    'program' : program,
    'cls' : clear,
    'docs' : docs,
    'google' : google
    
}

program_commands = {
    'info' : info
}

docs_query = {
    'python' : "https://docs.python.org/3/",
    'power panel' : "https://github.com/wesmags/Power-Panel/wiki"
}

google_commands = {
    'results' : results
}