# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных
# чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def summa(a: object, b: object) -> object:
    a+=1
    b-=1
    if b>0:
        return summa(a, b)
    else:
        return a

print(summa(2, 2))
