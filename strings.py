
s1 = "   Hello world  \t"
s2 = "Lol kek"

# конкатенация
print(s1 + s2)

# умножение на число n - дублирование n раз
print(s1*3)

# length
print(len(s1))

# убрать пробельные символы с начала и конца строки
print(s1.strip() + s2)

# разбить строку на список строк по некоторому символу
print(s1.split())

mas = [i*i for i in range(20) if i % 3 == 0]
print(mas)
print(*mas)
mas = [str(val) for val in mas]
print(mas)

# обединение массива строк с разделителем
print(" ".join(mas))
print("<>".join(mas))