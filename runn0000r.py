import json
import account0000r
from load0000rs import ethBalance, nonce
from analyz0000r import printBinaryTable

# secrets = json.load(open("secrets.json"))
# accounts = account0000r.accountsFromSecrets(secrets)
# accounts = account0000r.analyzeAccounts([nonce.load0000r(), ethBalance.load0000r()], accounts)
# account0000r.storeAccounts(accounts)

# some sample analysis
dataFile = "data/accounts-2022-07-06--21-50-57.json"
accounts = json.load(open(dataFile))

# all accounts with non-zero balance (ignoring dust)
nonZeroBalanceAccounts = list([ad["mnemonic"], ad["index"]] for ad in accounts if sum(list(v["ETH balance"]["nativeBalance"] for v in list(ad["chains"].values()))) > 0.001)
print("Accounts with non-zero balance on any chain:")
printBinaryTable(nonZeroBalanceAccounts)

# all accounts with non-zero balance
nonZeroNonceAccounts = list([ad["mnemonic"], ad["index"]] for ad in accounts if sum(list(v["nonce"]["nonce"] for v in list(ad["chains"].values()))) > 0 )
print("Accounts with non-zero nonce on any chain:")
printBinaryTable(nonZeroNonceAccounts)

# all accounts and chain names with non-zero balance
"""
for a in accounts:
    for c in a["chains"].items():
        if c[1]["ETH balance"]["nativeBalance"] > 0:
            print(f'{a["address"]} ({a["mnemonic"]}, account index {a["index"]}): {c[1]["ETH balance"]["nativeBalance"]} on {c[0]}')
"""

