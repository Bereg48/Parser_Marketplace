# Парсер для скачивания информации о товарах с сайта Ozon.

## Предназначение приложения:
- Парсинга данных с платформы Ozon данных о товарах по предоставленным кодам 
- Запись полученной информации в отдельный файл формата xls
- Вывод случайной статьи


### 1. Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости с помощью команд:
    Команда для Windows:
        1- python -m venv venv
        2- venv\Scripts\activate
        3- pip install -r requirements.txt

    Команда для Unix:
        1- python3 -m venv venv
        2- source venv/bin/activate 
        3- pip install -r requirements.txt


### 2. Для запуска приложения из командной строки:
        1-  python main.py


## Связь

Если у вас есть вопросы или предложения, можете связаться со мной по электронной почте: andreyanovi@yandex.ru

Особенности парсинга. Сервис Ozon закрыл свое API для официального парсинга данных о товарах, во избежании этото и соблюдения
требований заказчика разработан парсер который гибко и в соответсвии с правилами и существующими методами обхода ограничений
выгружает необходимые данные о товаре при этом скорость работы парсера ограничена требованиями сервиса Ozon.
Нет ограничений по колличеству запросов в соответсвии с корректной настройкой существующего парсера. 