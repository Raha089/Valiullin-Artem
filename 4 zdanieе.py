# 1 ЗАДАЧА
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
if A <= B:
    for i in range(A, B + 1):
        print(i)
else:
    print("A должно быть меньше или равно B")

# 2 ЗАДАЧА
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
if A < B:
    for i in range(A, B + 1):
        print(i)
else:
    for i in range(A, B - 1, -1):
        print(i)

# 3 ЗАДАЧА
A = int(input("Введите число A: ")) 
B = int(input("Введите число B: ")) 

if A > B:
  for i in range(A, B - 1, -1):
    if i % 2 != 0:
      print(i)
else:
  print("A должно быть больше B")

# 4 ЗАДАЧА
N = int(input("Введите количество чисел: "))
sum = 0

for i in range(N):
    sum += int(input("Введите число: "))

print("Сумма введенных чисел:", sum)

# 5 ЗАДАЧА
n = int(input("число n: "))
if n <= 0:
    print("n должно быть натуральным")
else:
    res = (n * (n + 1) // 2) ** 2
    print("Сумма кубов натуральных чисел от 1 до", n, "равна", res)

# 6 ЗАДАЧА
n = int(input("n="))
if n < 0:
    print("Факториаk только для натуралов")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print("n= ", factorial)

# 7 ЗАДАЧА
n = int(input("Введите n: "))
if n < 0:
    print("n должно быть натуралом")
else:
    factorial = 1
    sum1 = 0

    for i in range(1, n + 1):
        factorial *= i
        sum1 += factorial

    print(sum1)

# 8 ЗАДАЧА
n = int(input("Введите натуральное число ментше девяти"))

if 1 <= n <= 9:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
else:
    print("очибяка")

# 9 ЗАДАЧА
def fiba_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    fib_sum = 0
    fib_prev = 0
    fib_cur = 1
    for i in range(2, n + 1):
        fib_next = fib_prev + fib_cur
        fib_sum += fib_cur
        fib_prev = fib_cur
        fib_cur = fib_next
    return fib_sum
n = int(input("Ведите кол-во чисел из ряда фибаначи"))
result = fiba_sum(n)
print(result)