import json

from web3 import Web3
w3 = Web3(Web3.HTTPProvider('http://104.248.81.215:8545'))
w3.eth.default_account = w3.eth.accounts[0]

def get_privatekey():
    return w3.eth.account.decrypt({"address":"490cd3cabed9f706055e617ed09f96a905e0bd31",
                                   "crypto":{"cipher":"aes-128-ctr","ciphertext":"236e9e7c8c2ed5c54a96db44e3aee10f7d4418951dd70cf4b84e7d32d3f878ee",
                                             "cipherparams":{"iv":"04a18d6df851fe5ec114943ac08043db"},"kdf":"scrypt",
                                             "kdfparams":{"dklen":32,"n":262144,"p":1,"r":8,"salt":"1c4ad47842fcdbcf4a48ae2c118f472d85bb29a675fd6e0c1ae499378acec8ad"},
                                             "mac":"c15222a449abec6c4f3de61f742df5bb203ee50124758c92daa79bfdc2316c0e"},"id":"20768524-dd04-4acd-9bc9-1c819be4c0ea",
                                   "version":3}, 'root')


def hello_world():
    if (w3.isConnected()):
        print("Connecting to Node succesful")

        # latest block
        # print(w3.eth.get_block('latest'))
        trufflefile = json.load(open('./ABI/HelloWorld.json'))
        abi = trufflefile['abi']
        contract = w3.eth.contract(address='0x5d810f1295Dd14a7f57Ce7360EC86905D90528A3', abi=abi)
        answer = contract.functions.getGreeting().call()
        return("Response: " + answer)
    else:
        return("Connecting to Node failed")

# TODO
#def list_accounts():
