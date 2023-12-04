# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
#
# # Загрузка кодов товаров из файла
# with open('codes.txt', 'r') as f:
#     codes = f.read().splitlines()
#
# # Создание пустого DataFrame для хранения данных
# df = pd.DataFrame(columns=['Код товара', 'Название товара', 'URL страницы с товаром', 'URL первой картинки', 'Цена базовая', 'Цена с учетом скидок без Ozon Карты', 'Цена по Ozon Карте', 'Продавец', 'Количество отзывов', 'Количество видео', 'Количество вопросов', 'Рейтинг товара', 'Все доступные характеристики товара', 'Информация о доставке в Москве', 'Уцененный товар'])
#
# # Парсинг каждого товара
# for code in codes:
#     url = f'https://www.ozon.ru/product/{code}'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # Здесь нужно получить все необходимые данные с помощью BeautifulSoup
#     # Например, для названия товара:
#     name_element = soup.find('input', {'class': 'x7u tsBody500Medium'})
#     name = name_element.text if name_element else 'No name'
#
#     # Заполнение DataFrame
#     df = pd.concat([df, pd.DataFrame({'Код товара': [code], 'Название товара': [name]})], ignore_index=True)
#
# # Сохранение DataFrame в файл
# df.to_excel('products.xlsx', index=False)

import pandas as pd
import requests
from bs4 import BeautifulSoup

# Загрузка кодов товаров из файла
with open('codes.txt', 'r') as f:
    codes = f.read().splitlines()

# Создание пустого DataFrame для хранения данных
df = pd.DataFrame(columns=['Код товара', 'Название товара', 'URL страницы с товаром', 'URL первой картинки', 'Цена базовая', 'Цена с учетом скидок без Ozon Карты', 'Цена по Ozon Карте', 'Продавец', 'Количество отзывов', 'Количество видео', 'Количество вопросов', 'Рейтинг товара', 'Все доступные характеристики товара', 'Информация о доставке в Москве', 'Уцененный товар'])

# Парсинг каждого товара
for code in codes:
    url = f'https://www.ozon.ru/product/{code}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Получение названия товара
    name_elements = soup.findAll('div', class_='n4i n5i')
    print(name_elements)

    # Поиск элемента с тегом 'h1' среди найденных элементов
    name_element = next((element for element in name_elements if element.name == 'h1'), None)

    # Извлечение текста из найденного элемента или, в случае его отсутствия, присвоение значения 'No name'
    name = name_element.text if name_element else 'No name'

    # Получение URL страницы с товаром
    page_url = url

    # Получение URL первой картинки
    image_element = soup.find('img')
    image_url = image_element.get('src') if image_element else ''

    # Получение цены базовая
    base_price_element = soup.find('div', {'class': 'b3d2'})
    base_price = base_price_element.text.strip() if base_price_element else ''

    # Получение цены со скидкой без Ozon Карты
    discount_price_element = soup.find('div', {'class': 'v1c8'})
    discount_price = discount_price_element.text.strip() if discount_price_element else ''

    # Получение цены по Ozon Карте
    ozon_card_price_element = soup.find('div', {'class': 'k6x1'})
    ozon_card_price = ozon_card_price_element.text.strip() if ozon_card_price_element else ''

    # Получение продавца
    seller_element = soup.find('a', {'class': 'k3r7'})
    seller = seller_element.text.strip() if seller_element else ''

    # Получение количества отзывов
    reviews_element = soup.find('a', {'class': 'b1oq'})
    reviews_count = reviews_element.text.strip() if reviews_element else ''

    # Получение количества видео
    videos_element = soup.find('a', {'class': 'b2gr'})
    videos_count = videos_element.text.strip() if videos_element else ''

    # Получение количества вопросов
    questions_element = soup.find('span', {'class': 'b7e6'})
    questions_count = questions_element.text.strip() if questions_element else ''

    # Получение рейтинга товара
    rating_element = soup.find('div', {'class': 'd7g9'})
    rating = rating_element.text.strip() if rating_element else ''

    # Получение всех доступных характеристик товара
    characteristics_element = soup.find('ul', {'class': 'd7y9'})
    characteristics = characteristics_element.text.strip() if characteristics_element else ''

    # Получение информации о доставке в Москве
    delivery_info_element = soup.find('div', {'class': 'd9b9'})
    delivery_info = delivery_info_element.text.strip() if delivery_info_element else ''

    # Получение информации об уцененном товаре
    damaged_element = soup.find('div', {'class': 'd7b1'})
    damaged_info = damaged_element.text.strip() if damaged_element else ''

    # Заполнение DataFrame
    df = pd.concat([df, pd.DataFrame({'Код товара': [code], 'Название товара': [name], 'URL страницы с товаром': [page_url], 'URL первой картинки': [image_url], 'Цена базовая': [base_price], 'Цена с учетом скидок без Ozon Карты': [discount_price], 'Цена по Ozon Карте': [ozon_card_price], 'Продавец': [seller], 'Количество отзывов': [reviews_count], 'Количество видео': [videos_count], 'Количество вопросов': [questions_count], 'Рейтинг товара': [rating], 'Все доступные характеристики товара': [characteristics], 'Информация о доставке в Москве': [delivery_info], 'Уцененный товар': [damaged_info]})], ignore_index=True)

# Сохранение DataFrame в файл
df.to_excel('products.xlsx', index=False)


# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
#
# # Загрузка кодов товаров из файла
# with open('codes.txt', 'r') as f:
#     codes = f.read().splitlines()
#
# # Создание пустого DataFrame для хранения данных
# df = pd.DataFrame(columns=['Код товара', 'Название товара', 'URL страницы с товаром', 'URL первой картинки', 'Цена базовая', 'Цена с учетом скидок без Ozon Карты', 'Цена по Ozon Карте', 'Продавец', 'Количество отзывов', 'Количество видео', 'Количество вопросов', 'Рейтинг товара', 'Все доступные характеристики товара', 'Информация о доставке в Москве', 'Уцененный товар'])
#
# # Инициализация веб-драйвера
# driver = webdriver.Chrome()
#
# # Парсинг каждого товара
# for code in codes:
#     url = f'https://www.ozon.ru/product/{code}'
#
#     # Загрузка страницы товара с помощью веб-драйвера
#     driver.get(url)
#
#     # Получение HTML-кода страницы
#     page_source = driver.page_source
#
#     # Создание объекта BeautifulSoup для парсинга HTML-кода
#     soup = BeautifulSoup(page_source, 'html.parser')
#
#     # Получение названия товара
#     name_element = soup.find(class_='nl4').find('h1')
#     name = name_element.text.strip() if name_element else 'No name'
#
#     # Получение URL страницы с товаром
#     page_url = url
#
#     # Получение URL первой картинки
#     image_element = soup.find('img')
#     image_url = image_element.get('src') if image_element else ''
#
#     # Получение цены базовая
#     base_price_element = soup.find('div', {'class': 'b3d2'})
#     base_price = base_price_element.text.strip() if base_price_element else ''
#
#     # Получение цены со скидкой без Ozon Карты
#     discount_price_element = soup.find('div', {'class': 'v1c8'})
#     discount_price = discount_price_element.text.strip() if discount_price_element else ''
#
#     # Получение цены по Ozon Карте
#     ozon_card_price_element = soup.find('div', {'class': 'k6x1'})
#     ozon_card_price = ozon_card_price_element.text.strip() if ozon_card_price_element else ''
#
#     # Получение продавца
#     seller_element = soup.find('a', {'class': 'k3r7'})
#     seller = seller_element.text.strip() if seller_element else ''
#
#     # Получение количества отзывов
#     reviews_element = soup.find('a', {'class': 'b1oq'})
#     reviews_count = reviews_element.text.strip() if reviews_element else ''
#
#     # Получение всех доступных характеристик товара
#     characteristics_element = soup.find('ul', {'class': 'd7y9'})
#     characteristics = characteristics_element.text.strip() if characteristics_element else ''
#
#     # Получение информации о доставке в Москве
#     delivery_info_element = soup.find('div', {'class': 'd9b9'})
#     delivery_info = delivery_info_element.text.strip() if delivery_info_element else ''
#
#     # Получение информации об уцененном товаре
#     damaged_element = soup.find('div', {'class': 'd7b1'})
#     damaged_info = damaged_element.text.strip() if damaged_element else ''
#
#     # Заполнение DataFrame
#     df = pd.concat([
#         df, pd.DataFrame({
#             'Код товара': [code],
#             'Название товара': [name],
#             'URL страницы с товаром': [page_url],
#             'URL первой картинки': [image_url],
#             'Цена базовая': [base_price],
#             'Цена с учетом скидок без Ozon Карты': [discount_price],
#             'Цена по Ozon Карте': [ozon_card_price],
#             'Продавец': [seller],
#             'Количество отзывов': [reviews_count],
#             'Все доступные характеристики товара': [characteristics],
#             'Информация о доставке в Москве': [delivery_info],
#             'Уцененный товар': [damaged_info]
#         })
#     ], ignore_index=True)
#
# # Закрытие веб-драйвера
# driver.quit()
#
# # Сохранение DataFrame в файл
# df.to_excel('products.xlsx', index=False)