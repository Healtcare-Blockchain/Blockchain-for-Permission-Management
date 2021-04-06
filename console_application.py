from cmd import Cmd

import colorama
from art import text2art
from colorama import Fore

import account_functions as acf
import permission_functions as pmf


class MyPrompt(Cmd):
    prompt = '»'
    intro = Fore.BLUE + text2art("Blockchain Healthcare") + "\n Welcome! Type ? to list commands"

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

        if inp == 'hello world' or inp == 'hw' or inp == 'Hello World':
            return self.do_hello_world(inp)

        # if inp == 'latest':
        #     return self.do_latest_block(inp)

        print("{} is not a known command".format(inp))

    def do_exit(self, inp):
        '''exit the application.'''
        print("Challaz!")
        return True

    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')

    def do_Change_Web3_Settings(self, inp):
        '''change the settings of the Web3 Provider'''
        print("not implemented")

    def do_hello_world(self, inp):
        '''Use the hello world contract to test for a return'''
        print (Fore.RED + acf.hello_world())

    def do_set_permission(self, inp):
        '''Set permission between two adresses'''
        sender = input("Sender adress: ")
        they = input("Receiver adress: ")
        print(pmf.set_permission(sender, they))

    def do_check_permission(self, inp):
        '''check permission between two adresses'''
        print(pmf.check_permission())

    def do_get_accounts(self, inp):
        print()

    def do_get_privatekey(self, inp):
        print(acf.get_privatekey())

    do_EOF = do_exit
    help_EOF = help_exit

colorama.init(autoreset=True)
MyPrompt().cmdloop()