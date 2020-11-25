# Вариант с листом.
seasons = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
month = int(input("Введите цифрой какой сейчас месяц: "))
for i in range(len(seasons)):
    if month in seasons[i]:
        if i==0:
            print("Сейчас зима!")
        elif i==1:
            print("Сейчас весна!")
        elif i==2:
            print("Сейчас лето!")
        elif i==3:
            print("Сейчас осень!")
if month > 12:
    print("Нет такого месяца!")

# Вариант с листом и словарем.
my_list = ['зима', 'весна', 'лето', 'осень']
my_dict = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень'}
while True:
    season = int(input("Введите номер месяца (в диапазоне от 1 до 12): "))
    if 0 < season < 13:
        break
    else:
        print("Введены некорректные данные. Ознакомьтесь с условием.")
        continue
season -= 3

print("Список: ", my_list[(season // 3)+1 if 0 <= (season//3) < 3 else 0])
print("Словарь: ", my_dict.get((season // 3)+1 if 0 <= (season//3) < 3 else 0))






#time_of_year = dict(winter='[12, 1, 2]', spring='[3, 4, 5]', summer='[6, 7, 8]', autumn='[9, 10, 11]')
# month_1 = int(input("Введите цифрой какой сейчас месяц: "))
# if month_1 in time_of_year.values():
#     print(time_of_year.keys())