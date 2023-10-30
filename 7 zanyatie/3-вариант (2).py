def F(a):
    for i in range(len(a)):
        if a[i] < 15:
            a[i] *= 2
    print(a)


F([10, 20, 5, 14, 18, 13, 25, 11])
