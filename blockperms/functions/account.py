from . import blockchain

def unlock_account(address, passphrase):
    w3 = blockchain.connection_setup()
    try:
        w3.geth.personal.unlock_account(address, passphrase)
    except:
        raise
    else:
        print("Account unlocked")

def list_accounts():
    w3 = blockchain.connection_setup()
    return w3.eth.accounts
