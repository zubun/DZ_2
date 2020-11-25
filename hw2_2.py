#2.Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
product_list = []
execution = True
while execution == True:
    product_list.append(input("Введите список продуктов: "))
    execution = bool(int(input("Для дополнения списка введите 1, для завершения списка введите 0:")))
print(product_list)
#print(len(product_list))
for el in range(int(len(product_list)/2)):
        product_list[el], product_list[el + 1] = product_list[el + 1], product_list[el]
        el += 2
print(product_list)
