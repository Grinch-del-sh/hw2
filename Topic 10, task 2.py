# Запрашиваем границы диапазона
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# Определяем шаг: если start > end, идём вниз, иначе вверх
step = -1 if start > end else 1

# Создаём словарь
my_dict = {}

# Цикл от start до end (включительно) с шагом step
for k in range(start, end + step, step):
    my_dict[k] = k ** k

# Выводим результат
print(my_dict)