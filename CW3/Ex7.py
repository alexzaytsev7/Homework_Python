# Задача спирального заполнения матрицы

n = int(input())
matrix = [[0] * n for _ in range(n)]
dx, dy, x, y = 0, 1, 0, 0

for i in range(1, n * n+1):
    matrix[x][y] = i
    if matrix[(x+dx) % n][(y+dy) % n]:
        dx, dy = dy, -dx
    y+=dy
    x+=dx

for line in matrix:
    print(*(f'{i:<4}' for i in line), sep='')
