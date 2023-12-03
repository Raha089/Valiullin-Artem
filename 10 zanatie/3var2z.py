def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]


def swap_columns(matrix, i, j):
    for row in matrix:
        row[i], row[j] = row[j], row[i]


def find_max_element(matrix):
    max_element = matrix[0][0]
    max_row = 0
    max_col = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
                max_row = i
                max_col = j

    return max_element, max_row, max_col


input_file = open("Валиуллин_У-234_vvod2.txt", "r")
output_file = open("Валиуллин_У-234_vivod2.txt", "w")

n, m = map(int, input_file.readline().strip().split())

matrix = [list(map(float, input_file.readline().strip().split())) for _ in range(n)]

max_element, max_row, max_col = find_max_element(matrix)

swap_rows(matrix, 0, max_row)
swap_columns(matrix, 0, max_col)

for row in matrix:
    output_file.write(" ".join(map(str, row)) + "\n")

input_file.close()
output_file.close()
