from web3 import Web3
from settings import *
from abi import TOKEN_ABI
import address

def sendSHM(account):
    try:
        print("new query")
        web3 = Web3(Web3.HTTPProvider(RPC_URL))
        nonce = web3.eth.get_transaction_count(WALLET_ADDR)
        tx = {
            'nonce': nonce,
            'to': account,
            'value': web3.to_wei(15, 'ether'),
            'gas': 6000000,
            'gasPrice': web3.to_wei('2000', 'gwei')}

        signed_tx = web3.eth.account.sign_transaction(tx, WALLET_PK)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print("send")
        return web3.to_hex(tx_hash)
    except Exception as e:
        print(f"ERROR: {e}\nContinue...")
        return None


def check_tx(tx_hash, address) -> bool:
    try:
        data = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=20)
        if 'status' in data and data['status'] == 1:
            print(f"{address} | transaction was sucsessfull: {tx_hash}")
            return True
        else:
            print(f"{address} | transaction failed {data['transactionHash'].hex()}")
            return False
    except Exception as err:
        print(f"{address} | unexpected error in <check_tx> function: {err}")
        return False


def main():
    while True:
        new_addr_list = []
        for i in address.address_list:
            if not check_tx(sendSHM(i), i):
                new_addr_list.append(i)
            else:
                continue
        print(new_addr_list)
        address.address_list = new_addr_list
        if len(new_addr_list) == 0:
            break

main()
