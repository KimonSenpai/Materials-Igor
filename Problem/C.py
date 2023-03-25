mas = []

while True:
    a = int(input())
    if a == 0:
        break
    mas.append(a)

mx = max(mas)
s = 0

for i in range(len(mas)):
    if mas[i] == mx:
        s += 1

print(s)

