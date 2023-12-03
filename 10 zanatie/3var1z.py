def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(value) for value in line.split()]
            matrix.append(row)
    return matrix

def write_result_to_file(file_path, is_symmetric):
    with open(file_path, 'w') as file:
        file.write("Матрица симметрична" if is_symmetric else "Матрица несимметрична")

def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


file_path_input = "Валиуллин_У-234_vvod.txt"
file_path_output = "Валиуллин_У-234_vivod1.txt"

matrix = read_matrix_from_file(file_path_input)

symmetric = is_symmetric(matrix)

write_result_to_file(file_path_output, symmetric)
