def F(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True


matrix = [[10, 20, 30], [20, 40, 50], [30, 50, 60]]

if F(matrix):
    print("Матрица симметрична относительно главной диагонали.")
else:
    print("Матрица не симметрична относительно главной диагонали.")
