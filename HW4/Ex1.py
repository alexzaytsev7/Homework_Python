#Выдать без повторений в поряждке возрастания все те числа , которые встречаются в обоих наборах (множествах).

# group1 = {'1', '7', '7', '4', '5'}
# group2 = {'2', '7', '0', '7', '5'}
print('Кол-во элементов 1-го множества:')
n = int(input())
print('Кол-во элементов 2-го множества:')
m = int(input())
group1 = set()
group2 = set()
for i in range(n):
    group1.add(input())
for i in range(m):
    group2.add(input())
print('Множество 1 ', group1)
print('Множество 2 ', group2)

group3 = sorted(group1.intersection(group2))
print(group3)
