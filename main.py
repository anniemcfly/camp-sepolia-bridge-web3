import os
from dotenv import load_dotenv

from src.sender import send_from_camp_to_sepolia, send_from_sepolia_to_camp
from src.connection import connect_to_networks


load_dotenv()


def main():

    camp_web3, sepolia_web3 = connect_to_networks()
    print("Соединение установлено!")

    print("Укажите адрес кошелька. (Если нажать Enter, то данные возьмутся из файла .env)")
    to_address = input("Ответ: ")

    print("Укажите приватный ключ кошелька. (Если нажать Enter, то данные возьмутся из файла .env)")
    from_address_private = input("Ответ: ")

    print("Укажите сеть, из которой будет осуществляться транзакция (1 - Sepolia, 2 - Camp)")
    choice_network = int(input("Ответ: "))

    print("Укажите сумму перевода в ETH (Например: 0.001)")
    amount = input("Ответ: ")

    if len(to_address) < 10:
        to_address = os.getenv("WALLET_ADDRESS")

    if len(from_address_private) < 10:
        from_address_private = os.getenv("WALLET_PRIVATE_KEY")

    if choice_network == 1:
        sepolia_amount = sepolia_web3.to_wei(amount, 'ether')

        send_from_sepolia_to_camp(to_address, sepolia_amount, from_address_private, sepolia_web3)
    elif choice_network == 2:
        camp_amount = camp_web3.to_wei(amount, 'ether')

        send_from_camp_to_sepolia(to_address, camp_amount, from_address_private, camp_web3)


if __name__ == "__main__":

    while True:
        main()

        choice = input("Вы желаете провести ещё одну транзакцию? [y/n]")

        if choice == 'n':
            exit(0)
        elif choice == 'y':
            continue
        else:
            exit(1)
