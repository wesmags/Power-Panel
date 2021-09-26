
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
        


power_tools = Program("Windows Power Tools", 0.1)

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

commands = {
    # Dict full of accessers for comamnds - command : "command_call"
    'help' : help,
	'test' : test,
    'program' : program
    
}

program_commands = {
    'info' : info
}