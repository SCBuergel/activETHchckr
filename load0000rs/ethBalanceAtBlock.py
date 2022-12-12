import json
from web3 import Web3
from load0000rs.base import baseLoad0000r

class load0000r(baseLoad0000r):
    def name(self):
        return "ETH balance at block"

    def version(self):
        return "0.0.1"

    def analyze(self, account, chain):
        chains = json.load(open("chains.json"))
        chainIndex = chains.index(chain)
        blockNumbersEnd2021 = json.load(open("data/blockNumbersEnd2021.json"))
        targetBlockNumber = blockNumbersEnd2021[chainIndex]

        web3 = Web3(Web3.HTTPProvider(chain["api"]))
        balance = web3.eth.getBalance(account, targetBlockNumber)/1e18
        newEntry = self.createEmptyAccountEntry()
        newEntry["nativeBalance"] = balance
        return newEntry



