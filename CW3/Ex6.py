# Дан одноиерный массив числовых значений, насчитывающий N элементов.
# Вместо каждого 0-го элемента поставить сумму 2-х предыдущих.

a = [1, 5, 0, 3, 0, 1, 1, 0, 9]
print(a)
for i in range(len(a)):
    if a[i] == 0 and i != 0:
        b = a[i-2]+a[i-1]
        a[i] = b
print(a)
