import json
from web3 import Web3
from cmd import Cmd
from art import text2art
import colorama
from colorama import Fore, Back

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8085'))
w3.eth.default_account = w3.eth.accounts[0]

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

def set_permission():
    if (w3.isConnected()):
        print("Connecting to Node succesful")


        trufflefile = json.load(open('./ABI/UserPermissions.json'))
        abi = trufflefile['abi']
        permissions_contract = w3.eth.contract(address='0x1aF4522DE8AD97869909EBd0987BFB879670d556', abi=abi);

        print(w3.eth.accounts[0])
        sender = '0x490CD3cAbED9f706055e617Ed09F96a905E0BD31';
        they = '0x50b72d23E5F3c1E0002E2E4C44C2f01ddd605b6F';

        # sender = w3.eth.accounts[0];
        # they = w3.eth.accounts[1];

        # permissions_contract.functions.setPermissions(w3.eth.accounts[1], w3.eth.accounts[0], True).call();
        # gas_estimate = permissions_contract.functions.setPermissions(w3.eth.accounts[0], w3.eth.accounts[1], True).estimateGas();
        # print(f'Gas estimate to transact with set_permission: {gas_estimate}')

        print(f'Sending transaction to manage permission for: {sender} \n')

        permission = permissions_contract.functions.setPermissions(sender, they, True).transact();
        receipt = w3.eth.waitForTransactionReceipt(permission)
        print("Transaction receipt mined:")
        print(dict(receipt))
        print("\nWas transaction successful?")
        print(receipt["status"])

        return("Succes?" + permission)

    else:
        return("Connecting to Node failed")

def check_permission():
    if (w3.isConnected()):
        print("Connecting to Node succesful")
        trufflefile = json.load(open('./ABI/UserPermissions.json'))
        abi = trufflefile['abi']
        contract = w3.eth.contract(address='0x1aF4522DE8AD97869909EBd0987BFB879670d556', abi=abi);
        sender = '0x490CD3cAbED9f706055e617Ed09F96a905E0BD31';
        they = '0x50b72d23E5F3c1E0002E2E4C44C2f01ddd605b6F';
        permission = contract.functions.getPermitted(sender, they).call();
        if permission == True:
            set_permission = "Permission granted";
        elif permission == False:
            set_permission = "permission not granted";
        return("Succes: " + set_permission)
    else:
        return("Connecting to Node failed")

def get_privatekey():
    return w3.eth.account.decrypt({"address":"490cd3cabed9f706055e617ed09f96a905e0bd31",
                                   "crypto":{"cipher":"aes-128-ctr","ciphertext":"236e9e7c8c2ed5c54a96db44e3aee10f7d4418951dd70cf4b84e7d32d3f878ee",
                                             "cipherparams":{"iv":"04a18d6df851fe5ec114943ac08043db"},"kdf":"scrypt",
                                             "kdfparams":{"dklen":32,"n":262144,"p":1,"r":8,"salt":"1c4ad47842fcdbcf4a48ae2c118f472d85bb29a675fd6e0c1ae499378acec8ad"},
                                             "mac":"c15222a449abec6c4f3de61f742df5bb203ee50124758c92daa79bfdc2316c0e"},"id":"20768524-dd04-4acd-9bc9-1c819be4c0ea",
                                   "version":3}, 'root');
#todo

# def get_permission_mapping_length():
#     if (w3.isConnected()):
#         print("Connecting to Node succesful")
#         trufflefile = json.load(open('./ABI/UserPermissions.json'))
#         abi = trufflefile['abi']
#         contract = w3.eth.contract(address='0x84544C22037099685163773Fedbc852efFD4e2D0', abi=abi);
#         length = contract.functions.getMappingLength().call();
#         return("Succes:" + length)
#     else:
#         return("Connecting to Node failed")




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

    def do_set_permission(self, inp):
        '''Set permission between two adresses'''
        print(set_permission());

    def do_check_permission(self, inp):
        '''check permission between two adresses'''
        print(check_permission());

    # def do_get_permission_mapping_length(self, inp):
    #     print(get_permission_mapping_length());

    def do_get_accounts(self, inp):
        print(w3.eth.get_accounts());

    def do_get_privatekey(self, inp):
        print(get_privatekey())

    do_EOF = do_exit
    help_EOF = help_exit

colorama.init(autoreset=True)
MyPrompt().cmdloop()