# 1 ЗАДАНИЕ
a = int(input("Введите а:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))
d = a + b + c
print("Сумма a+b+c=", d)

# 2 ЗАДАНИЕ
a = int(input("Длинна 1 катета="))
b = int(input("Длинна второго катета="))
S = 1 / 2 * a * b
print("Площадь прямоугольного треугольника равна", S)
Ы
# 3 ЗАДАНИЕ
n = int(input("Колличество минут прошедших с начала суток="))
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, (":"), minutes)

# 4 ЗАДАНИЕ
a = int(input("Расстояние между рядами="))
b = int(input("Расстояние между дырочками в ряду="))
l = int(input("Колличество дырочек в ряду="))
N = int(input("Длинна свободного конца шнурка="))
print(2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)

# 5 ЗАДАНИЕ
a = int(input("Первое число="))
b = int(input("Второче число="))
c = int(input("Третье число="))
if a < b:
    if a < c:
        y = a
    else:
        y = c
else:
    if b < c:
        y = b
    else:
        y = c
print("Наименьшее:", y)

# 6 ЗАДАНИЕ
a1 = int(input("Строка первой клетки:"))
b1 = int(input("Столбец первой клетки:"))
a2 = int(input("Строка второй клетки:"))
b2 = int(input("Столбец второй клетки"))
if (a1 + b1 + a2 + b2) % 2 == 0:
    print("Да")
else:
    print("Нет")

    # 7 ЗАДАНИЕ
    a = int(input("Год:"))
if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
    print("Да")
else:
    print("Нет")

# 8 ЗАДАНИЕ
a = int(input("Первое число="))
b = int(input("Второе число="))
c = int(input("Тертье число="))
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

# 9 ЗАДАНИЕ
n = int(input("n="))
m = int(input("m="))
k = int(input("k="))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("Да")
else:
    print("Нет")
