mas = []
lmax = 0
while True:
    a = int(input())
    if a == 0:
        break
    mas.append(a)


for i in range(1, len(mas) - 1):
    if mas[i] > mas[i+1] and mas[i] > mas[i-1]:
        lmax += 1

print(lmax)