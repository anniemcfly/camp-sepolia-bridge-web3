# Запуск

 - Клонируем на устройство: `git clone https://github.com/anniemcfly/camp-sepolia-web3.git`
 - Заходим в папку: `cd camp-sepolia-web3`
 - Создаём виртуальное окружение Python: `python -m venv venv`
 - Заходим в него: `source venv/bin/activate`
 - Устанавливаем необходимые библиотеки: `pip install -r requirements.txt`
 - При желании создаём файл `.env` и вносим в него две переменные `WALLET_ADDRESS` и `WALLET_PRIVATE_KEY`.
 - Запускаем скрипт: `python main.py`

# Настройка

 Конфигурационный файл находиться по этому пути: `src/config.py`. Внутри него можно настройть RPC endpoint.

