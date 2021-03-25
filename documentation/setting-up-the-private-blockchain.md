# Setting up the private blockchain

## Setting up locally

### Installing dependencies:

First we will install the dependencies we need for the private ethereum blockchain.

```bash
$ brew tap ethereum/ethereum
$ brew install ethereum
```

### Creating the file scructure:

Next we will setup our project structure:

First create a folder lets call it "Ethereum smart contracts".   
In this folder create a file called "genesis.json" open this file with you editor of choice and copy the following into the file:

```bash
genesis.json
{
    "config": {
        "chainId": 987, 
        "homesteadBlock": 0,
        "eip150Block": 0, 
        "eip155Block": 0, 
        "eip158Block": 0},

    "nonce": "0x0000000000000042",
    "timestamp": "0x0",
    "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "extraData": "0x00",
    "gasLimit": "0x8000000",
    "difficulty": "0x400",
    "mixhash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "coinbase": "0x3333333333333333333333333333333333333333",
    "alloc": {}
    
}
```

Then create a folder in the earlier created folder in which we are going to save our node. Lets call it "blkchain".

### Starting the blockchain:

#### Initialize the blockchain

```
$ geth --rpc --rpcport "8085" --datadir ./blkchain init genesis.json
```

#### Start the blockchain

```text
$ geth --rpc --rpcport "8085" --datadir ./blkchain --networkid 123 --nodiscover
```

The blockchain is now running.

### Using the blockchain

To acces the blockchain go into the folder that you created for you blockchain and start a terminal here.

```text
$ geth attach geth.ipc 
```

Succes! You now have acces to your blockchain.

