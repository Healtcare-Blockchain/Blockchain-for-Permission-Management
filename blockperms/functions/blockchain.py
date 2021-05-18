from web3 import Web3
from web3.middleware import geth_poa_middleware

def connection_setup():
    try:
        w3 = Web3(Web3.HTTPProvider('http://5ece2cdfad16.ngrok.io'))

        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    except ConnectionError as ce:
        print('Error establishing connection')
        raise ce
    else:
        return w3
