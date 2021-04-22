import json

from web3 import Web3


def connection_setup():
    w3 = Web3(Web3.HTTPProvider('http://104.248.81.215:8545'))
    w3.eth.default_account = w3.eth.accounts[0]
    return w3

def set_permission(sender, they):
    w3 = connection_setup()
    if (w3.isConnected()):
        print("Connecting to Node succesful")
        w3.geth.personal.unlock_account(sender, "")
        w3.geth.personal.unlock_account(they, "")
        trufflefile = json.load(open('contracts/abi/UserPermissions.json'))
        abi = trufflefile['abi']
        permissions_contract = w3.eth.contract(address='0x7c32Cd419D003dEDcc3EC161B20296d3A42b465F', abi=abi)

        # sender = '0x490CD3cAbED9f706055e617Ed09F96a905E0BD31';
        # they = '0x50b72d23E5F3c1E0002E2E4C44C2f01ddd605b6F';

        permissions_contract.functions.setPermissions(sender, they, True).call()
        gas_estimate = permissions_contract.functions.setPermissions(w3.eth.accounts[0], w3.eth.accounts[1], True).estimateGas()
        print(f'Gas estimate to transact with set_permission: {gas_estimate}')

        print(f'Sending transaction to manage permission for: {sender} \n')

        permission = permissions_contract.functions.setPermissions(sender, they, True).transact()
        receipt = w3.eth.waitForTransactionReceipt(permission)
        print("Transaction receipt mined:")
        print(dict(receipt))
        print("\nWas transaction successful?")
        print(receipt["status"])

        return("Succes?" + permission)

    else:
        return("Connecting to Node failed")

def check_permission(sender, they):
    w3 = connection_setup()
    if (w3.isConnected()):
        print("Connecting to Node succesful")
        trufflefile = json.load(open('contracts/abi/UserPermissions.json'))
        abi = trufflefile['abi']
        contract = w3.eth.contract(address='0x7c32Cd419D003dEDcc3EC161B20296d3A42b465F', abi=abi)
        # sender = '0x490CD3cAbED9f706055e617Ed09F96a905E0BD31'
        # they = '0x50b72d23E5F3c1E0002E2E4C44C2f01ddd605b6F'
        permission = contract.functions.getPermitted(sender, they).call()
        if permission:
            set_permission = "Permission granted"
        elif not permission:
            set_permission = "permission not granted"
        return("Succes: " + set_permission)
    else:
        return("Connecting to Node failed")