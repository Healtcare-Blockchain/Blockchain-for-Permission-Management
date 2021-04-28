from web3 import Web3
from web3.middleware import geth_poa_middleware

def connection_setup():
    try:
        w3 = Web3(Web3.HTTPProvider('http://104.248.81.215:8545'))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    except:
        raise
    else:
        print(w3.clientVersion)
        return w3
