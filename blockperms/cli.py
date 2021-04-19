import cmd2
import argparse
from art import text2art
from blockperms.functions import account, permission

import colorama

#todo change cmd to cmd2

class MyPrompt(cmd2.Cmd):
    #ducks ="    _      _      _     _      _      _     _      _      _ \n""__(.)< __(.)> __(.)= __(.)< __(.)> __(.)= __(.)< __(.)> __(.)= \n""\___)  \___)  \___) \___)  \___)  \___) \___)  \___)  \___) "
    prompt = '»'
    intro = colorama.Fore.BLUE + text2art("Block-Perms") + "\n Welcome! Type ? to list commands"

    def default(self, args):
        if args == 'x' or args == 'q':
            return self.do_exit(args)

        if args == 'hello world' or args == 'hw' or args == 'Hello World':
            return self.do_hello_world(args)

        # if inp == 'latest':
        #     return self.do_latest_block(inp)

        print("{} is not a known command".format(args))

    def do_exit(self, args):
        '''exit the application.'''
        print("Challaz!")
        return True

    def do_Ruben1701(self, args):
        '''About the creator of Block-Perms'''
        self.poutput("    __\n___( o)> This project was started for a school project\n\ <_. )  Github: https://github.com/Ruben1701\n `---'")

    def help_exit(self):
        self.poutput('exit the application. Shorthand: x q Ctrl-D.')

    def do_Change_Web3_Settings(self, args):
        '''change the settings of the Web3 Provider'''
        self.poutput(colorama.Fore.RED +"not implemented")

    def do_hello_world(self, args):
        '''Use the hello world contract to test for a return'''
        print (colorama.Fore.RED + account.hello_world())

    set_permission_parser = argparse.ArgumentParser()
    set_permission_parser.add_argument('-np', '--nopass', action='store_true', help='If account is already unlocked some other way')
    set_permission_parser.add_argument('permission', nargs='+', help='The permission to set True | False')

    @cmd2.with_argparser(set_permission_parser)
    def do_set_permission(self, args):
        '''Set permission between two adresses'''
        self.poutput(args.permission)
        print(args.permission)
        sender = input("Sender adress: ")
        sender_pass = input("Sender password: ")
        they = input("Receiver adress: ")
        they_pass = input("Receiver password: ")
        print(permission.set_permission(sender, they))

    def do_check_permission(self, args):
        '''check permission between two adresses'''
        print(permission.check_permission())

    def do_get_accounts(self, args):
        print()

    def do_get_privatekey(self, args):
        print(account.get_privatekey())

    do_EOF = do_exit
    help_EOF = help_exit

colorama.init(autoreset=True)
MyPrompt().cmdloop()