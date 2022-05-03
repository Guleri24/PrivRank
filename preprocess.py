import csv
import random


def write_csv(matrix):
    with open('similarity.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        for row in matrix:
            writer.writerow(row)


def f():
    N = 1000  # 1000 -> N; Also need to change in main.py; obfuscation() call
    res = [[1 for _ in range(0, N)] for _ in range(0, N)]
    for i in range(0, N):
        for j in range(i, N):
            if i != j:
                x = random.random()
                res[i][j] = x
                res[j][i] = x
    return res


result = f()
write_csv(result)
