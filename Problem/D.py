mas = []
s = 1
mx = 0
lv = 0

while True:
    a = int(input())
    if a == 0:
        break
    mas.append(a)

if len(mas) != 0:
    mx = 1

for i in range(1, len(mas)):
    if mas[i] == mas[i-1]:
        lv = 0
        s = 1
    elif mas[i] > mas[i-1]:
        if lv == -1:
            s = 2
            lv = 1
        else:
            s += 1
            lv = 1
    else:
        if lv == 1:
            s = 2
            lv = -1
        else:
            s += 1
            lv = -1
    if s > mx:
        mx = s

print(mx)



