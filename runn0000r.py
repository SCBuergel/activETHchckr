import json
import account0000r
from load0000rs import ethBalance, nonce

secrets = json.load(open("secrets.json"))
accounts = account0000r.accountsFromSecrets(secrets)
accounts = account0000r.analyzeAccounts([nonce.load0000r(), ethBalance.load0000r()], accounts)
account0000r.storeAccounts(accounts)

# some sample analysis - printing all accounts and chain names with non-zero balance
dataFile = "data/accounts-2022-07-04--22-30-36.json"
accounts = json.load(open(dataFile))
for a in accounts:
    for c in a["chains"].items():
        if c[1]["ETH balance"]["nativeBalance"] > 0:
            print(f'{a["address"]} on {c[0]}')



