s = 1
mx = 0
mas = []


while True:
    a = int(input())
    if a == 0:
        break
    mas.append(a)

if len(mas) != 0:
    mx = 1

for i in range(len(mas)-1):
    if mas[i] == mas[i + 1]:
        s += 1
        if s > mx:
            mx = s

    elif mas[i] != mas[i+1]:
        s = 1

print(mx)





