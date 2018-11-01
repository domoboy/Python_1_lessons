# Транспонирование матрицы

matrix = [[0.5, 0, 0, 0, 0],
          [1, 0.5, 0, 0, 0],
          [1, 1, 0.5, 0, 0],
          [1, 1, 1, 0.5, 0],
          [1, 1, 1, 1, 0.5]]

# Транспонирование
matrix_t = list(zip(*matrix))  # zip - застежка, сцепливает, * здесь распаковка

# Вывод матрицы
# print(matrix)
# print(matrix_t)

print('*' * 15)

for item in matrix_t:
    print(list(item))