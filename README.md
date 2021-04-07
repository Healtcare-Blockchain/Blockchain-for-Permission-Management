# Blockchain Permission Management

[![Build Status](https://travis-ci.com/Ruben170/Blockchain-for-Permission-Management.svg?branch=main)](https://travis-ci.com/Ruben170/Blockchain-for-Permission-Management)

> Managing permissions on the blockchain not because we need to but because we can.

## Glossary

1. About the project
2. Getting started

### About the project

This project started as a schoolproject from Fontys ICT in collaboration with Peercode. It is a Python project that interacts with a private ethereum network. This blockchain has a smart contract which is being used to manage the permissions between different accounts. This can be used in many different usecases.

#### Quick project breakdown

![Project Breakdown 1.0](https://documents.lucid.app/documents/3aa1f67a-c1f8-44f5-875d-ced1a5271091/pages/YRprA5eG3Zio?a=8548&x=95&y=-1238&w=990&h=1276&store=1&accept=image%2F*&auth=LCA%20f2cc9be68c12069b752a21519a4ec3e21a6ec74c-ts%3D1617264406)

The above image consists of 2 systems which again consists of multiple containers:

**The 2 Systems**

1. **The permission management application** This is the python application which interacts with the blockchain. Further explained when we get into the containers.
2. **The private Ethereum Blockchain** This is the same as the Ethereum Blockchain only hosted on a private network. This was chosen for multiple reasons which we wil go into on this page: **ADD PAGE FOR PRIVATE BLOCKCHAIN CHOICE**

**The Containers**

1. **The API** The API is a restfull python [Fast API](https://fastapi.tiangolo.com). Fast API is a quick to set-up and readable api which should be easy to work with by anyone with coding experience. The api is made so that users can create theyre own applications which can interact with the permissions management application.
2. **The Console Application** A easy to use command line interface which can be used to monitor and change the blockchain. This is for users that want to interact with the blockchain but dont want to create an entire application that uses the API or for quick debugging.
3. **Blockchain Functions** The blockchain functions are used by both the API and the Console Application. The blockchain functions make use of web3.py which is a python library that makes use of web3 which is the standard wrapper for interacting with a Ethereum Blockchain.
4. **UserPermissions** This is a smart contract which is "running" on the blockchain. The smart contract is written in solidity and contains a mapping of the users account hash and a true or false for the permission. \(this will be updated to also give permissions for certain topics\).

