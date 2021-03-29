# Private Ethereum netwerk
_Documentversie 1.0.0_
## Introductie
Het eindproduct van deze challenge wordt een verzameling van systemen die medische data kan delen. Een van die systemen is het toegangsrechtensysteem die de toegang regelt tot patiëntendata. Binnen het toegangsrechtensysteem wordt gebruik gemaakt van een private ethereum blockchain. Hierop gaan we de smartcontracts deployen en laten draaien.

## Achtergrond informatie
Een netwerk is in de context van Ethereum een verzameling van nodes die verbonden zijn met elkaar. Deze nodes draaien een Ethereum client. Een client is een applicatie die Ethereum implementeert.[²][@NodesClients]
Elke client kan een API blootstellen naar de buitenwereld. Via deze API kunnen applicaties verbinding leggen met een node.[³][@JSONRPCAPI]

Een private Ethereum blockchain is een netwerk dat niet vrij toegangelijk is. Het netwerk is dus niet openbaar. Private betekent in deze context achtergehouden en/of geisoleerd.[¹][@Networks]

## Configuratie van het netwerk
Voor de nodes maken we gebruik van geth. Dit is een ethereum client geschreven in de programmeertaal Go. Dit is de meest voorkomende client met de grootste userbase.[²][@NodesClients]

### Globale settings
#### Network id
```
55
```

#### JSON-RPC API URL
```
http://104.248.81.215:8545
```

#### Genesis block
See <https://github.com>.
##### Consensus algorithm
```
Proof of Authority
```

##### Signer accounts
```
0x69f87bf57da1db2ff0e1e837915c3df018911408
```

### Miner node settings

#### Miner node enode
```
"enode://9a38545f795599368083741f873fb5a260b04e79d57b84f064da5cd987db8fcf3c10d903edf98501becb3d277c2b115e2de7b34cdc72a25c0ffccbfecb742fe8@104.248.81.215:30303"
```

#### Miner node enr
```
"enr:-J24QAF8CTeR-YqDxdRu6zG0PvlFP8KI1ajFJJQFLgVso3X7J_Kv7xNP-9gR6m17WplZrP6jfCk3LPQE6qWFz0UXjq0Og2V0aMfGhABGUQmAgmlkgnY0gmlwhGj4UdeJc2VjcDI1NmsxoQKaOFRfeVWZNoCDdB-HP7WiYLBOedV7hPBk2lzZh9uPz4RzbmFwwIN0Y3CCdl-DdWRwgnZf"
```

#### Miner node id
```
"enr:-J24QAF8CTeR-YqDxdRu6zG0PvlFP8KI1ajFJJQFLgVso3X7J_Kv7xNP-9gR6m17WplZrP6jfCk3LPQE6qWFz0UXjq0Og2V0aMfGhABGUQmAgmlkgnY0gmlwhGj4UdeJc2VjcDI1NmsxoQKaOFRfeVWZNoCDdB-HP7WiYLBOedV7hPBk2lzZh9uPz4RzbmFwwIN0Y3CCdl-DdWRwgnZf"
```

#### Miner node genesis
```
"0x328cea3299b1e42d7e158efec83450502027701df59560e2ea605656d3ea6621"
```

#### Miner node enode
```
"enode://78846af2efa24d4283fc285caf0fff201ba8ed2d02018ec6147839f9b3ed77aa72ad1d8f1f74f18c6384723df38d99937b9480deea09cb67484567c9aea78077@104.248.81.215:30305"
```

#### Miner node enr
```
"enr:-J24QFtzI8QsVhlmJWnmEy2qPbwvXnk0WJwpXia_U5bNsxYJc-nE8Nvr1WNku89VcwZJ6ZVMOuQwV_ng-cP0g_g0NLcCg2V0aMfGhABGUQmAgmlkgnY0gmlwhGj4UdeJc2VjcDI1NmsxoQN4hGry76JNQoP8KFyvD_8gG6jtLQIBjsYUeDn5s-13qoRzbmFwwIN0Y3CCdmGDdWRwgnZh"
```

#### Miner node id
```
"5183bc47d17214ace8baf8719efcf8e2ead3fe6365cee4bc60e1f8fa1babab40"
```

#### Miner node genesis
```
"0x328cea3299b1e42d7e158efec83450502027701df59560e2ea605656d3ea6621"
```
## Gebruik van het netwerk

### Toevoegen van member node


## Bronnen
1. ethereum.org. ‘Networks’. Accessed 29 March 2021. [https://ethereum.org/en/developers/docs/networks/][@Networks].
2. ethereum.org. ‘Nodes and Clients’. Accessed 29 March 2021. [https://ethereum.org/en/developers/docs/nodes-and-clients/][@NodesClients].
3. ethereum.org. ‘JSON-RPC API’. Accessed 23 March 2021. [https://ethereum.org/en/developers/docs/apis/json-rpc/][@JSONRPCAPI].

[@NodesClients]: https://ethereum.org/en/developers/docs/nodes-and-clients/
[@Networks]: https://ethereum.org/en/developers/docs/networks/
[@JSONRPCAPI]: https://ethereum.org/en/developers/docs/apis/json-rpc/