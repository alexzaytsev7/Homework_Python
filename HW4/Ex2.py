#group1 = [1, 7, 6, 8, 1]
# {'1', '7', '7', '4', '5'}
print("Кол-во клумб:")
n = int(input())
group1 = [int(input("Введите кол-во черники на каждой клумбе ")) for i in range(n)]
print(group1)
n_digits = set(group1)

numax1 = 0
numax2 = 0
for i in range(len(group1)):
    numax1 = group1[i-2]+group1[i-1]+group1[i]
    if numax1 > numax2:
        numax2 = numax1
print(numax2)
