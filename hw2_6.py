#6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
stop = 1
accounting_book = []
number = 1
analytics_name =[]
analytics_article_number = []
analytics_count = []
analytics_price = []
while stop !=0:
#Структура данных товары.
    name = input("Введите наименование: ")
    article_number = input("Введите артикул: ")
    price = int(input("Введите цену товара: "))
    count = int(input("Введите кол-во на складе: "))
    product = {'name':name, 'article_number':article_number, 'price':price, 'count':count}
    tuple = (number, product)
    number += 1
    accounting_book.append(tuple)
#Аналитика
    analytics_name.append(name)
    analytics_article_number.append(article_number)
    analytics_price.append(price)
    analytics_count.append(count)
    stop = int(input("Для прекращения ввода товаров введите 0, для продолжения введите 1:"))
analytics = {'Наименование':analytics_name, 'Артикул':analytics_article_number, 'Цена':analytics_price, 'Кол-во на складе':analytics_count}
print("-" * 30)
print("Список имеющихся товаров на складе ")
print("-" * 30)
for el in range(len(accounting_book)):
    print(accounting_book[el])
print("-" * 30)
print("Аналитика товаров на складе:")
print("-" * 30)
for key, val in analytics.items():
    print(f"{key} {val}")
print("-" * 30)
