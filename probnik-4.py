
mas = [int(val) for val in input().split()]

mx = max(mas)

s = 0
i = 0
while i < len(mas):
    if mas[i] == mx:
        mas.insert(i+1, s)
        if mas[i] > 0: s += mas[i]
        i += 2
    else:
        if mas[i] > 0: s += mas[i]
        i += 1

mas = map(str, mas)
print(" ".join(mas))    