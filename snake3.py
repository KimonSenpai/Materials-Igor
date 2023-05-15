n, m = (int(val) for val in input().split())

matr = [[0]*m for i in range(n)]


for i in range(n):
    for j in range(m):
        cnt = i*m
        if i % 2 == 0:
            cnt += j
        else:
            cnt += m - j - 1
        matr[i][j] = cnt


for i in range(n):
    print(*matr[i])