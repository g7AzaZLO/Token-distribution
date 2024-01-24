from web3 import Web3
from web3.middleware import geth_poa_middleware

RPC_URL = ""
web3 = Web3(Web3.HTTPProvider(RPC_URL))
def get_private():
    web3.eth.account.enable_unaudited_hdwallet_features()
    account = web3.eth.account.from_mnemonic("")
    private_key = account._private_key
    return private_key

WALLET_PK = get_private()