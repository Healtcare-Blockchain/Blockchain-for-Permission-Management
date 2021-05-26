import json
import logging

from web3 import Web3

from . import blockchain
from . import account

def set_permission(sender, sender_pass, receiver, receiver_pass, permission):
    w3 = blockchain.connection_setup()
    if (w3.isConnected()):
        # sender = w3.toChecksumAddress(sender)
        # they = w3.toChecksumAddress(they)
        logging.info("Connecting to Node succesful")
        account.unlock_account(sender, sender_pass)
        account.unlock_account(receiver, receiver_pass)

        trufflefile = json.load(open('contracts/abi/UserPermissions.json'))
        abi = trufflefile['abi']
        permissions_contract = w3.eth.contract(address='0xde200A090A976AC656A8DaA5ae7ac1d7D3F0aB70', abi=abi)

        permissions_contract.functions.setPermissions(sender, receiver, permission).call()
        gas_estimate = permissions_contract.functions.setPermissions(sender, receiver, permission).estimateGas()
        logging.info(f'Gas estimate to transact with set_permission: {gas_estimate}')

        logging.info(f'Sending transaction to manage permission for: {sender} \n')

        nonce = w3.eth.get_transaction_count('0x490CD3cAbED9f706055e617Ed09F96a905E0BD31')
        transact = permissions_contract.functions.setPermissions(sender, receiver, permission).buildTransaction({'nonce': nonce})

        signed_transact = w3.eth.account.sign_transaction(transact, private_key='0x8909ba431927ac8315de16dc867be6c5571360c2728d59d52a767457d94e7abd')
        permissiontx = w3.eth.sendRawTransaction(signed_transact.rawTransaction)
        receipt = w3.eth.waitForTransactionReceipt(permissiontx)
        logging.info("Transaction receipt mined:")
        logging.info(dict(receipt))

        return(str(receipt["status"]))

    else:
        logging.error('Failed to connect to node')
        return("Connecting to Node failed")

def check_permission(sender, they):
    w3 = blockchain.connection_setup()
    if (w3.isConnected()):
        print("Connecting to Node succesful")
        trufflefile = json.load(open('contracts/abi/UserPermissions.json'))
        abi = trufflefile['abi']
        contract = w3.eth.contract(address='0xde200A090A976AC656A8DaA5ae7ac1d7D3F0aB70', abi=abi)
        permission = contract.functions.getPermitted(sender, they).call()
        if permission:
            set_permission = "Permission granted"
        elif not permission:
            print(permission)
            set_permission = "permission not granted"
        return(set_permission)
    else:
        return("Connecting to Node failed")