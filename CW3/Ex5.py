# Даны две различные клетки шахматной доски. Напишите программу,
# которая определяет, может ли король попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и
# номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES», если из первой клетки ходом короля можно попасть
# во вторую, или «NO» в противном случае.

list_1 =input("Введите 4 числа от 1 до 8 ").split()

for k in range(len(list_1)):
    list_1[k] = int(list_1[k])
result_list = []

print(list_1)

if abs(int(list_1[0]) - int(list_1[2])) <=1 & abs(int(list_1[1]) - (int(list_1[2]))) <= 1:
    #if int(list_1[1]) == int(list_1[3]) + 1:
    print("Yes")
else:
    print('No')