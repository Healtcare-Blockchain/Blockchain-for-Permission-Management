import json
from . import blockchain

def unlock_account(address, passphrase):
    w3 = blockchain.connection_setup()
    try:
        w3.geth.personal.unlock_account(address, passphrase)
    except:
        raise
    else:
        print("Account unlocked")

# TODO
#def list_accounts():
