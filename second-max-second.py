
max1 = 0
max2 = 0
while True:
    val = int(input())
    if val == 0:
        break
    
    if val > max1:
        max2 = max1
        max1 = val
    elif val <= max1 and val > max2:
        max2 = val


print(max2)
