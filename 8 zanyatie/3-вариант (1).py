import math


def C(a, b):
    C1 = math.sqrt(a**2 + b**2)
    return C1


# Для первого треугольника
a1 = float(input("Введите длину первого катета: "))
b1 = float(input("Введите длину второго катета: "))
C1 = C(a1, b1)

# Для второго
a2 = float(input("Введите длину первого катета второго треугольника: "))
b2 = float(input("Введите длину второго катета второго треугольника: "))
C2 = C(a2, b2)

if C1 > C2:
    print("Гипотенуза первого треугольника больше.")
elif C2 > C1:
    print("Гипотенуза второго треугольника больше.")
else:
    print("Гипотенузы равны по длине.")
