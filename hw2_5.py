
line = input("введите рейтинг: ")
top = []
the_converted_rating = []
top = line.split()
the_converted_rating = list(map(int,top))
# print(top)
the_converted_rating.sort(reverse = True)
# print(sorted(the_converted_rating, reverse =True))
print(the_converted_rating)

# my_top = [7, 6, 4, 4, 2, 2, 1]
number = int(input("Введите рейтинг.Для выхода введите 666: "))
while number!=666:
    for el in range(len(the_converted_rating)):
        if the_converted_rating[el] == number:
            #position_1 = the_converted_rating.index(el)
            the_converted_rating.insert(el +1, number)
            break

        elif the_converted_rating[el] > number and the_converted_rating[el +1] < number:
            #position_1 = the_converted_rating.index(el)
            the_converted_rating.insert(el + 1, number)
            break

        elif the_converted_rating[0] < number:
            #position_1 = the_converted_rating.index(el)
            the_converted_rating.insert(0, number)
            break

        elif the_converted_rating[-1] > number:
            #position_1 = the_converted_rating.index(el)
            the_converted_rating.append(number)
            break

    print(f"Вы ввели число {number}. Рейтинговый список:{the_converted_rating}")
    number = int(input("Введите рейтинг.Для выхода введите 666: "))