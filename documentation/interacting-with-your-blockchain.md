---
description: How to interact with the private ethereum blockchain using Geth
---

# Interacting with your blockchain

{% hint style="info" %}
The geth commands mentioned in this tutorial are the same commands powering the blockchain API
{% endhint %}

## Getting into the interactive shell

To interact with our blockchain we will acces the chain using geths interactive javascript enviroment:

```
#Make sure you are in the folder used for your blockchain
$geth attach geth.ipc
```

You should see a response as follows:

```bash
Welcome to the Geth JavaScript console!
```

## Creating an account

To start mining Ethereum, creating and sending transactions and using/deploying Solidity smart contracts you will need an account:

{% hint style="info" %}
You should be in the interactive geth console
{% endhint %}

```bash
personal.newAccount()
```

Then when asked to set a password create a password for this account and write it down. You will need this in later steps.

## Starting the miner

### 

