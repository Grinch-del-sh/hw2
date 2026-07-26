# Функция для вычисления факториала числа (итеративно)
def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


# Ввод натурального числа с клавиатуры
n = int(input("Enter a natural number: "))

# Вычисляем факториал введённого числа
f = factorial(n)

# Строим список факториалов чисел от f до 1 в убывающем порядке
factorials_list = [factorial(i) for i in range(f, 0, -1)]

# Выводим результат
print(factorials_list)
