n, m = (int(val) for val in input().split())

matr = [[0]*m for i in range(n)]

cnt = 0

for i in range(n):
    if i%2 == 0:
        for j in range(m):
            matr[i][j] = cnt
            cnt += 1
    else:
        for j in range(m - 1, -1, -1):
            matr[i][j] = cnt
            cnt += 1

for i in range(n):
    print(*matr[i])