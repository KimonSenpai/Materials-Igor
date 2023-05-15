n, m = (int(val) for val in input().split())

matr = [[0]*m for i in range(n)]


for cnt in range(n*m):
    i = cnt // m
    j = cnt % m
    if i % 2 == 1:
        j = m - cnt%m - 1
    matr[i][j] = cnt

for i in range(n):
    print(*matr[i])