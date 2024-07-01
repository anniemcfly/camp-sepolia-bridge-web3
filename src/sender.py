from web3 import Web3

from src.gas import get_estimate_gas, get_base_fee


def send_from_camp_to_sepolia(to_address: str, amount, private_key: str, web3_: Web3):
    """Осуществляет перевод ETH из сети Camp в сеть Sepolia"""

    from_account = web3_.eth.account.from_key(private_key)
    nonce = web3_.eth.get_transaction_count(from_account.address)

    transaction = {
        'from': from_account.address,
        'to': to_address,
        'value': amount,
        'nonce': nonce,
        'gas': get_estimate_gas(from_account.address, to_address, amount, web3_),
        'gasPrice': get_base_fee(web3_),
    }

    signed = web3_.eth.account.sign_transaction(transaction, private_key)
    tx_hash = web3_.eth.send_raw_transaction(signed.rawTransaction)

    print(f"Транзакция выполнена успешно!. Хэш транзакции: {tx_hash.hex()}")


def send_from_sepolia_to_camp(to_address: str, amount, private_key: str, web3_: Web3):
    """Осуществляет перевод ETH из сети Sepolia в сеть CAMP"""

    from_account = web3_.eth.account.from_key(private_key)
    nonce = web3_.eth.get_transaction_count(from_account.address)

    transaction = {
        'from': from_account.address,
        'to': to_address,
        'value': amount,
        'nonce': nonce,
        'gas': get_estimate_gas(from_account.address, to_address, amount, web3_),
        'gasPrice': get_base_fee(web3_),
    }

    signed = web3_.eth.account.sign_transaction(transaction, private_key)
    tx_hash = web3_.eth.send_raw_transaction(signed.rawTransaction)

    print(f"Транзакция выполнена успешно!. Хэш транзакции: {tx_hash.hex()}")
