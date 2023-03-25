mas = []
lmax = 0
index1 = 0

while True:
    a = int(input())
    if a == 0:
        break
    mas.append(a)

mnlen = len(mas)

for i in range(1, len(mas) - 1):
    if mas[i] > mas[i+1] and mas[i] > mas[i-1]:
        if i - index1 < mnlen and index1 != 0:
            mnlen = i - index1
        index1 = i
if mnlen == len(mas):
    mnlen = 0


print(mnlen)