import json
from web3 import Web3
from cmd import Cmd
from art import text2art
import colorama
from colorama import Fore, Back

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8085'))

def hello_world():
    if (w3.isConnected()):
        print("Connecting to Node succesful")

        # latest block
        # print(w3.eth.get_block('latest'))
        trufflefile = json.load(open('./ABI/HelloWorld.json'))
        abi = trufflefile['abi']
        contract = w3.eth.contract(address='0x5d810f1295Dd14a7f57Ce7360EC86905D90528A3', abi=abi);
        answer = contract.functions.getGreeting().call();
        return("Response: " + answer)
    else:
        return("Connecting to Node failed")


class MyPrompt(Cmd):
    prompt = '»'
    intro = Fore.BLUE + text2art("Blockchain Healthcare") + "\n Welcome! Type ? to list commands"

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)


        if inp == 'hello world' or inp == 'hw' or inp == 'Hello World':
            return self.do_hello_world(inp)

        if inp == 'latest':
            return self.do_latest_block(inp)

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
        print (Fore.RED + hello_world())

    def do_latest_block(self, inp):
        '''Get latest block on the chain'''
        print(w3.eth.get_block('latest'))

    do_EOF = do_exit
    help_EOF = help_exit

colorama.init(autoreset=True)
MyPrompt().cmdloop()