def F(x):
    sum = 0
    n = len(x)

    print("Массив D:", x)

    for i in range(1, n, 2):
        sum += x[i]

    print("Сумма элементов с нечетными индексами:", sum)


S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
F(S)
