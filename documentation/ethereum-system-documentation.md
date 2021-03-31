# Ethereum systeem documentatie
```
Documentversie 1.1.0
```
## Introductie
Het eindproduct van deze challenge wordt een verzameling van systemen die medische data kan delen. Een van die systemen is het toegangsrechtensysteem die de toegang regelt tot patiëntendata. Het toegangsrechtensysteem maakt gebruik van het Ethereumsysteem. Binnen dit systeem draait een private Ethereum netwerk. Op dit netwerk gaan we  smartcontracts deployen en laten draaien.

## Achtergrond informatie
Een netwerk is in de context van Ethereum een verzameling van nodes die verbonden zijn met elkaar. Deze nodes draaien een Ethereum client. Een client is een applicatie die Ethereum implementeert.[²][@NodesClients]
Elke client kan een API blootstellen naar de buitenwereld. Via deze API kunnen applicaties verbinding leggen met een node.[³][@EthereumClientAPI]

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
**Zie dit bestand in de GitHub repository. Link staat hieronder:**

```shell
https://github.com/Healtcare-Blockchain/Blockchain-for-Permission-Management/blob/main/documentation/genesis.json
```
##### Consensus algorithm
```
Proof of Authority
```

##### Signer accounts
```
0x69f87bf57da1db2ff0e1e837915c3df018911408
```

##### Private key van signer accounts
```
3d90219cda89d9d4d3d556e6c1d20a160f9520a7cf8b7a75507d1bf88ba8f00f
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

### Api node settings

#### Api node enode
```
"enode://78846af2efa24d4283fc285caf0fff201ba8ed2d02018ec6147839f9b3ed77aa72ad1d8f1f74f18c6384723df38d99937b9480deea09cb67484567c9aea78077@104.248.81.215:30305"
```

#### Api node enr
```
"enr:-J24QFtzI8QsVhlmJWnmEy2qPbwvXnk0WJwpXia_U5bNsxYJc-nE8Nvr1WNku89VcwZJ6ZVMOuQwV_ng-cP0g_g0NLcCg2V0aMfGhABGUQmAgmlkgnY0gmlwhGj4UdeJc2VjcDI1NmsxoQN4hGry76JNQoP8KFyvD_8gG6jtLQIBjsYUeDn5s-13qoRzbmFwwIN0Y3CCdmGDdWRwgnZh"
```

#### Api node id
```
"5183bc47d17214ace8baf8719efcf8e2ead3fe6365cee4bc60e1f8fa1babab40"
```

#### Api node genesis
```
"0x328cea3299b1e42d7e158efec83450502027701df59560e2ea605656d3ea6621"
```
## Gebruik van het netwerk

### Toevoegen van member node

### Inloggen op het signer account om smart contracts te deployen
Er wordt vanuit gegaan dat je geth hebt geïnstaleerd. En dat geth gebruiktmaakt van een data map genaamd `node_data_1`. Maak deze map aan of maak gebruik van een bestaande data map.

##### Zet private key in een bestand
```bash
# This is a bash shell \
echo "3d90219cda89d9d4d3d556e6c1d20a160f9520a7cf8b7a75507d1bf88ba8f00f" > privatekey.txt
```

##### Importeer private key in geth
```bash
# This is a bash shell \
geth --datadir node_data_1 account import privatekey.txt
```

##### Wachtwoord invullen
Er wordt dan gevraagd om een wachtwoord in te vullen. Dit wachwoord moet je zelf verzinnen. Met dit wachtwoord wordt de private key versleuteld. Het maakt niet uit wat je hier invult zolang je het maar onthoudt. 

##### Je bent nu klaar
Je krijgt nu het publieke adres te zien van het account wat je net hebt toegevoegd. Dit adres kan je nu gebruiken om mee te signen.

## Bronnen
1. ethereum.org. ‘Networks’. Accessed 29 March 2021. [https://ethereum.org/en/developers/docs/networks/][@Networks].
2. ethereum.org. ‘Nodes and Clients’. Accessed 29 March 2021. [https://ethereum.org/en/developers/docs/nodes-and-clients/][@NodesClients].
3. ethereum.org. ‘JSON-RPC API’. Accessed 23 March 2021. [https://ethereum.org/en/developers/docs/apis/json-rpc/][@EthereumClientAPI].

[@NodesClients]: https://ethereum.org/en/developers/docs/nodes-and-clients/
[@Networks]: https://ethereum.org/en/developers/docs/networks/
[@EthereumClientAPI]: https://ethereum.org/en/developers/docs/apis/json-rpc/