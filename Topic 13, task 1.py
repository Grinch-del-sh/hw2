# Импортируем модуль random для генерации случайных чисел
import random

def generate_matrix(rows, cols, min_val=-100, max_val=100):
    """
    Генерирует матрицу размером rows x cols со случайными числами
    в диапазоне от min_val до max_val (включительно).
    """
    matrix = []
    for _ in range(rows):
        row = [random.randint(min_val, max_val) for _ in range(cols)]
        matrix.append(row)
    return matrix

def print_matrix(matrix, name="Матрица"):
    """
    Выводит матрицу в удобном для чтения виде.
    """
    print(f"\n{name}:")
    for row in matrix:
        # Форматируем числа, чтобы выровнять по ширине (до 5 символов)
        formatted_row = " ".join(f"{num:>5}" for num in row)
        print(formatted_row)

def add_matrices(mat1, mat2):
    """
    Складывает две матрицы одинаковой размерности.
    Возвращает новую матрицу-сумму.
    """
    rows = len(mat1)
    cols = len(mat1[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

# ---------- Основная часть программы ----------

# Запрашиваем размеры матрицы у пользователя
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Генерируем две матрицы одинаковой размерности
matrix_1 = generate_matrix(rows, cols)
matrix_2 = generate_matrix(rows, cols)

# Выводим исходные матрицы
print_matrix(matrix_1, "Матрица 1")
print_matrix(matrix_2, "Матрица 2")

# Складываем матрицы
matrix_3 = add_matrices(matrix_1, matrix_2)

# Выводим результирующую матрицу
print_matrix(matrix_3, "Сумма матриц (Матрица 3)")