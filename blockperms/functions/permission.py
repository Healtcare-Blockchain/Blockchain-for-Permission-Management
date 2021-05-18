import json

from . import blockchain
from . import account


def set_permission(sender, sender_pass, they, they_pass):
    w3 = blockchain.connection_setup()
    if (w3.isConnected()):
        # sender = w3.toChecksumAddress(sender)
        # they = w3.toChecksumAddress(they)
        print("Connecting to Node succesful")
        account.unlock_account(sender, sender_pass)
        account.unlock_account(they, they_pass)

        trufflefile = json.load(open('contracts/abi/UserPermissions.json'))
        abi = trufflefile['abi']
        permissions_contract = w3.eth.contract(address='0xde200A090A976AC656A8DaA5ae7ac1d7D3F0aB70', abi=abi)

        permissions_contract.functions.setPermissions(sender, they, True).call()
        gas_estimate = permissions_contract.functions.setPermissions(sender, they, True).estimateGas()
        print(f'Gas estimate to transact with set_permission: {gas_estimate}')

        print(f'Sending transaction to manage permission for: {sender} \n')

        nonce = w3.eth.get_transaction_count(sender)
        transact = permissions_contract.functions.setPermissions(they, sender, True).buildTransaction({'nonce': nonce})

        signed_transact = w3.eth.account.sign_transaction(transact, private_key='0x8909ba431927ac8315de16dc867be6c5571360c2728d59d52a767457d94e7abd')
        permission = w3.eth.sendRawTransaction(signed_transact.rawTransaction)
        receipt = w3.eth.waitForTransactionReceipt(permission)
        print("Transaction receipt mined:")
        print(dict(receipt))

        return("Succes:" + str(receipt["status"]))

    else:
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
        return("Succes: " + set_permission)
    else:
        return("Connecting to Node failed")