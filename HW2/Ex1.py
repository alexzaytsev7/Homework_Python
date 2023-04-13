print("Введите кол-во монет на столе")
n=int(input())
num_zer = 0
num_1 = 0
print("введите положение монет: 0 - решка, 1 - орел")
for i in range(n):
    x = int(input())
    if x == 0:
        num_zer += 1
    else:
        num_1 += 1
if num_zer > num_1:
    print(num_1)
else:
    print(num_zer)