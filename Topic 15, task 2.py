# Родительский класс Transport
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"


# Дочерний класс Autobus, наследующий Transport
class Autobus(Transport):
    # Переопределяем метод seating_capacity с аргументом по умолчанию 50
    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


# Запрашиваем данные у пользователя
name = input("Введите название автобуса: ")
speed = int(input("Введите максимальную скорость: "))
mileage = int(input("Введите пробег: "))

# Создаём объект Autobus
bus = Autobus(name, speed, mileage)

# Вызываем метод seating_capacity без аргумента (используется значение по умолчанию)
print(bus.seating_capacity())