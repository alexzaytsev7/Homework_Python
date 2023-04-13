print ("Задайте сумму чисел ")
sum = int(input())
print ("Задайте произведение чисел ")
mult = int(input())
try:
    for i in range(sum):
        for j in range(mult):
            if sum == i+j and mult == i * j:
                print ("Задуманные числа ", i, j)
                raise StopIteration
except StopIteration:
    pass



