def find_max_element(matrix):
    max_value = None
    max_i, max_j = None, None

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if max_value is None or value > max_value:
                max_value = value
                max_i, max_j = i, j

    return max_i, max_j


def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]


def swap_columns(matrix, i, j):
    for row in matrix:
        row[i], row[j] = row[j], row[i]


def move_max_to_top_left(matrix):
    max_i, max_j = find_max_element(matrix)

    # Поменять местами строки
    swap_rows(matrix, 0, max_i)

    # Поменять местами столбцы
    swap_columns(matrix, 0, max_j)


# Пример использования
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Вызываем функцию для перемещения максимального элемента
move_max_to_top_left(matrix)

# Выводим результат
for row in matrix:
    print(row)
