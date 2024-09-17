matrix = [[0 for _ in range(7)] for _ in range(7)]

for i in range(7):
    for j in range(7 - i):
        matrix[i][j] = i + j + 1

for row in matrix:
    print(row)
