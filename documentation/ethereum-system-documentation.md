# Ethereum systeem documentatie
```
Documentversie 1.1.0
```
## Introductie
Het eindproduct van deze challenge wordt een verzameling van systemen die medische data kan delen. Een van die systemen is het toegangsrechtensysteem die de toegang regelt tot patiëntendata. Het toegangsrechtensysteem maakt gebruik van het Ethereumsysteem. Binnen dit systeem draait een private Ethereum netwerk. Op dit netwerk gaan we  smartcontracts deployen en laten draaien.

## Achtergrond informatie
Een netwerk is in de context van Ethereum een verzameling van nodes die verbonden zijn met elkaar. Deze nodes draaien een Ethereum client. Een client is een applicatie die Ethereum implementeert.[¹][@NodesClients]
Elke client kan een API blootstellen naar de buitenwereld. Via deze API kunnen applicaties verbinding leggen met een node.[²][@EthereumClientAPI]

Een private Ethereum blockchain is een netwerk dat niet vrij toegangelijk is. Het netwerk is dus niet openbaar. Private betekent in deze context achtergehouden en/of geisoleerd.[³][@Networks]

## Configuratie van het netwerk
Voor de nodes maken we gebruik van geth. Dit is een ethereum client geschreven in de programmeertaal Go. Dit is de meest voorkomende client met de grootste userbase.[¹][@NodesClients]

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
"enode://85544396e2f25705b2e6358c29d6704b827279781e9af4d2b51b1f599cfbc56e5c428f4108361f08d6d6baf4a65ebed896671f74f6f3b8752dcdc820d6cb3da7@104.248.81.215:30303?discport=0"
```

#### Miner node enr
```
"enr:-Ja4QE7KMGBsBdekoTMAUrpB9g4gNNyybKEr2hl-yuedz2X-U33yXCLG332rGUYcQFFTgdmqZR8Sir5YKLbSZbXnUBwCg2V0aMfGhAK_L1yAgmlkgnY0gmlwhGj4UdeJc2VjcDI1NmsxoQOFVEOW4vJXBbLmNYwp1nBLgnJ5eB6a9NK1Gx9ZnPvFboRzbmFwwIN0Y3CCdl8"
```

#### Miner node id
```
"d359d1ca09aab2139d4379e44d55518a5e063da385c9aae85294ac2b356eef6b"
```

#### Miner node genesis
```
"0x6c32a23f0ad9beb9608f1ab0da83532cf7932776a13cafd5d3a8f87d8cc0bc1f"
```

### Api node settings

#### Api node enode
```
"enode://d067e77bae467ab3e38a1d0da024f7c0ffd164b049047592aeb22e411c4d753a5746fa9b676df7efefd76fa5909ff371d2db9e550f9f98583f1c22d513487a9c@104.248.81.215:30305?discport=0"
```

#### Api node enr
```
"enr:-Ja4QC2jfBk6yKoIlGi4OThcwV_AUsdcaeCYS2tUbPx1G7LyO33L_eNyblGXbsgytv4egs9eFjbIu3HrIm1m_3qPJIwCg2V0aMfGhAK_L1yAgmlkgnY0gmlwhGj4UdeJc2VjcDI1NmsxoQLQZ-d7rkZ6s-OKHQ2gJPfA_9FksEkEdZKusi5BHE11OoRzbmFwwIN0Y3CCdmE"
```

#### Api node id
```
"e55950f3035a23d0fc99537fd423e78e2b71f0027342b01dc8ae2514bf510a76"
```

#### Api node genesis
```
"0x6c32a23f0ad9beb9608f1ab0da83532cf7932776a13cafd5d3a8f87d8cc0bc1f"
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