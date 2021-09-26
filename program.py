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
    pro_sub = input()


def info():

commands = {
    # Dict full of accessers for comamnds - command : "command_call"
    'help' : help,
	'test' : test
}

program_commands = {
    'info' : info
}