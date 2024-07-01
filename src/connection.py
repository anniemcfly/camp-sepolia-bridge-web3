from web3 import Web3
from web3.middleware import geth_poa_middleware

from src.config import CAMP_NETWORK_RPC_URL, SEPOLIA_NETWORK_RPC_URL


def connect_to_networks() -> tuple[Web3, Web3]:
    """Осуществляет подключение к сетям."""

    camp_web3 = Web3(Web3.HTTPProvider(CAMP_NETWORK_RPC_URL))
    camp_web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    sepolia_web3 = Web3(Web3.HTTPProvider(SEPOLIA_NETWORK_RPC_URL))
    sepolia_web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    return camp_web3, sepolia_web3
