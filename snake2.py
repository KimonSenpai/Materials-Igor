n, m = (int(val) for val in input().split())

matr = [[0]*m for i in range(n)]

cnt = 0

for i in range(n):
    for j in range(m):
        jj = j
        if i%2 == 1:
            jj = m - j - 1
        matr[i][jj] = cnt
        cnt += 1

for i in range(n):
    print(*matr[i])