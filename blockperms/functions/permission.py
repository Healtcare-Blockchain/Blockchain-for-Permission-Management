import json
import logging

from web3 import Web3

from . import blockchain
from . import account

def set_permission(sender, sender_pass, they, they_pass):
    w3 = blockchain.connection_setup()
    if (w3.isConnected()):
        print(w3.eth.accounts)
        print("Connecting to Node succesful")
        account.unlock_account(sender, sender_pass)
        account.unlock_account(they, they_pass)

        trufflefile = json.load(open('contracts/abi/UserPermissions.json'))
        abi = trufflefile['abi']
        permissions_contract = w3.eth.contract(address='0x7c32Cd419D003dEDcc3EC161B20296d3A42b465F', abi=abi)

        permissions_contract.functions.setPermissions(sender, they, True).call()
        gas_estimate = permissions_contract.functions.setPermissions(sender, they, True).estimateGas()
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
    w3 = blockchain.connection_setup()
    if (w3.isConnected()):
        print("Connecting to Node succesful")
        trufflefile = json.load(open('contracts/abi/UserPermissions.json'))
        abi = trufflefile['abi']
        contract = w3.eth.contract(address='0x7c32Cd419D003dEDcc3EC161B20296d3A42b465F', abi=abi)
        permission = contract.functions.getPermitted(sender, they).call()
        if permission:
            set_permission = "Permission granted"
        elif not permission:
            set_permission = "permission not granted"
        return("Succes: " + set_permission)
    else:
        return("Connecting to Node failed")