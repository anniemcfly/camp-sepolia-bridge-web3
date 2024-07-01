from web3 import Web3


def get_base_fee(web3_: Web3) -> int:
    """Проверка актуальной цены на газ."""

    current_gas_price = web3_.eth.gas_price
    print(f"Актуальная цена на газ: {current_gas_price}")

    return current_gas_price


def get_estimate_gas(from_address: str, to_address: str, amount, web3_: Web3):

    estimate_gas = web3_.eth.estimate_gas({
        'from': from_address,
        'to': to_address,
        'value': amount
    })

    return estimate_gas


def total_gas_coast(base_fee: float, estimate_gas: int, priority_fee: int | float = 0) -> float:
    """Производит подсчёт общей стоимости газа."""

    total_gas = estimate_gas * (base_fee + priority_fee)
    print(f"Общая сумма газа: {total_gas}")

    return total_gas
