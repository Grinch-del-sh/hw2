# Родительский класс Transport
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Класс Autobus, наследующий Transport
class Autobus(Transport):
    # Наследуем всё от родителя, ничего не добавляем
    pass

# Запрашиваем данные у пользователя
name = input("Введите название автомобиля: ")
speed = int(input("Введите максимальную скорость: "))
mileage = int(input("Введите пробег: "))

# Создаём объект Autobus
bus = Autobus(name, speed, mileage)

# Выводим информацию в требуемом формате
print(f"Название автомобиля: {bus.name} Скорость: {bus.max_speed} Пробег: {bus.mileage}")