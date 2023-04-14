n = int(input("Введите размер n: "))
m = int(input("Введите размер m: "))
k = int(input("Введите количество долек k: "))
z = m*n-k
if k < n * m and (k % n == 0 or k % m == 0):
    print("Yes")
else:print("No")