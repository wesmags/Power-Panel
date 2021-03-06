import subprocess
from googlesearch import search
import json
import webbrowser

from os import system, name
from time import sleep
import os 
import glob



# Find docs on curses and get it installing properly, use it for making a proper text editor in command line 
import curses

top_token = ":"
sub_token_1 = "-" + top_token
sub_token_2 = " $" + top_token

cmd_token = '$'
edit_token = ';'

protected_files = {
    "run.bat" : "run.bat",
    "program.py" : "program.py",
    "LICENSE" : "LICENSE",
    ".gitattributes" : ".gitattributes",
    ".gitignore" : ".gitignore",
    "config.JSON" : "config.JSON",
    "README.md" : "README.md"
    
}

def cmd_msg(welcome_info):
	print(welcome_info)
	sleep(1.5)
	clear()

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

def editor():
    editor_sub = input(sub_token_1)
    text_commands[editor_sub]()

# Opens Editor in New Window
#def editor():
#    os.chdir("directory")
#    os.startfile("editor.bat")

def editor():
    workdr = r"C:\Users\Wes Mags\Documents\Projects\Power Tools"
    filedir = r"\editor.bat"
    fulldr = workdr + filedir
    subprocess.call(fulldr)

def append():
    editor_mode = True
    filename = input("File Title: ")
    f = open(filename, "a")
    while editor_mode:
        text = input("          " + edit_token)
        if text != cmd_token + "EXIT":
            f.write(text + "\n")
        else:
            cmd_msg(filename + " saved succesfully")
            f.close()
            editor_mode = False
            break
            
def overwrite():
    editor_mode = True
    filename = input("File Title: ")
    f = open(filename, "w")
    while editor_mode:
        text = input("          " + edit_token)
        if text != cmd_token + "EXIT":
            f.write(text + "\n")
        else:
            cmd_msg(filename + " saved succesfully")
            f.close()
            editor_mode = False
            break
        
        

def read():
    filename = input("File Title: ")
    f = open(filename, "r")
    print(f.read())


def delete():
    cmd_msg("The delete command is a potentially dangerous function, proceed with caution")
    deletable = True
    filename = input("File Title: ")
    for accessor, func, in commands.items():
        if filename == accessor or filename == func:
            deletable = False
            pass
    if filename == "" or filename == cmd_token + "EXIT":
        deletable = False
        cmd_msg("Abandoning deletion")
        pass
    if os.path.exists(filename) and deletable == True:
      os.remove(filename)
      cmd_msg(filename + " deleted successfully from directory")
    else:
      print("The file does not exist")
      cmd_msg("Abandoning deletion")
    
def run():
    run_sub = input(sub_token_1)
    if run_sub == 'py':
        pyexe_sub = input(sub_token_2)
        subprocess.Popen('python ' + pyexe_sub +  ".py")
        
        # 
        print(">>>")
        
        if pyexe_sub == "":
            pass

def check_cd():
    print(sub_token_1 + str(os.getcwd()))
    
def change_d():
    path = input(sub_token_1)
    os.chdir(path)
    
def create_folder():
    print(" Enter folder name ")
    fname = input(sub_token_1)
    os.mkdir(fname)
    
def list_dir_f():
    print(str(os.listdir()))

def go_back():
    # string manip and stop at back slash 
    pass
    
commands = {
    # Dict full of accessers for comamnds - command : "command_call"
    'help' : help,
	'test' : test,
    'program' : program,
    'cls' : clear,
    'docs' : docs,
    'google' : google,
    'editor' : editor,
    'run' : run,
    'ccd' : check_cd,
    'cd' : change_d,
    'newfolder' : create_folder,
    'listf' : list_dir_f
    
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

text_commands = {
    'a' : append,
    'r' : read,
    'o' : overwrite,
    'd' : delete
}

