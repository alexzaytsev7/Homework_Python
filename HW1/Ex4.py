n = int(input("Введите размер n: "))
m = int(input("Введите размер m: "))
k = int(input("Введите количество долек k: "))
z = m*n-k
if n+m>k and z % m == 0:
    print("Yes")
    if n + m >= k and z%n == 0:
        print("Yes")
else:print("No")