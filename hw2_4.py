line = input("введите строку: ")
words = []
num = 1
words = line.split()
for el in range(line.count(' ') + 1):
    print(f" {num} {words [el] [0:10]}")
    num += 1