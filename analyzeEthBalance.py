from web3 import Web3
from analyzeBase import analyzeBase

class analyzeEthBalance(analyzeBase):
    def name(self):
        return "ETH balance"

    def version(self):
        return "0.0.1"

    def analyze(self, account, chain):
        web3 = Web3(Web3.HTTPProvider(chain["api"]))
        balance = web3.eth.getBalance(account)/1e18
        newEntry = self.createEmptyAccountEntry()
        newEntry["nativeBalance"] = balance
        return newEntry



