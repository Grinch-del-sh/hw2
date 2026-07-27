# Класс Черепашка (Turtle)
class Turtle:
    def __init__(self, x, y, s):
        """
        Конструктор: задаём начальные координаты и шаг.
        """
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        """Увеличивает y на s."""
        self.y += self.s

    def go_down(self):
        """Уменьшает y на s."""
        self.y -= self.s

    def go_left(self):
        """Уменьшает x на s."""
        self.x -= self.s

    def go_right(self):
        """Увеличивает x на s."""
        self.x += self.s

    def evolve(self):
        """Увеличивает шаг s на 1."""
        self.s += 1

    def degrade(self):
        """
        Уменьшает шаг s на 1.
        Если после уменьшения s станет <= 0, выбрасывает ошибку ValueError.
        """
        if self.s <= 1:
            raise ValueError("Невозможно уменьшить шаг: s станет <= 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        """
        Возвращает минимальное количество шагов (действий go_*),
        необходимое для достижения точки (x2, y2) при текущем шаге s.
        Считаем, что можно двигаться только в четырёх направлениях,
        каждый шаг смещает на s по одной из осей.
        Минимальное количество шагов = ceil(|dx|/s) + ceil(|dy|/s).
        """
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        # Функция ceil для целых чисел: (a + s - 1) // s
        steps_x = (dx + self.s - 1) // self.s if dx > 0 else 0
        steps_y = (dy + self.s - 1) // self.s if dy > 0 else 0
        return steps_x + steps_y


# ------------------------------------------------------------
# Демонстрация работы класса (интерактивный ввод)
# ------------------------------------------------------------

print("=== Класс Черепашка ===")
# Ввод начальных параметров
try:
    x = int(input("Введите начальную координату x: "))
    y = int(input("Введите начальную координату y: "))
    s = int(input("Введите начальный шаг s (целое положительное число): "))
    if s <= 0:
        print("Шаг должен быть положительным. Установлено s = 1.")
        s = 1
except ValueError:
    print("Введены некорректные данные. Установлены значения по умолчанию: x=0, y=0, s=1.")
    x, y, s = 0, 0, 1

turtle = Turtle(x, y, s)
print(f"Черепашка создана: x={turtle.x}, y={turtle.y}, s={turtle.s}")

# Демонстрация методов (пользователь вводит команды)
print("\nДоступные команды:")
print("up, down, left, right, evolve, degrade, moves x2 y2, stop")

while True:
    cmd = input("\nВведите команду: ").strip().lower()
    if cmd == 'stop':
        print("Работа завершена.")
        break
    elif cmd == 'up':
        turtle.go_up()
        print(f"Новая позиция: x={turtle.x}, y={turtle.y}")
    elif cmd == 'down':
        turtle.go_down()
        print(f"Новая позиция: x={turtle.x}, y={turtle.y}")
    elif cmd == 'left':
        turtle.go_left()
        print(f"Новая позиция: x={turtle.x}, y={turtle.y}")
    elif cmd == 'right':
        turtle.go_right()
        print(f"Новая позиция: x={turtle.x}, y={turtle.y}")
    elif cmd == 'evolve':
        turtle.evolve()
        print(f"Шаг увеличен: s={turtle.s}")
    elif cmd == 'degrade':
        try:
            turtle.degrade()
            print(f"Шаг уменьшен: s={turtle.s}")
        except ValueError as e:
            print(f"Ошибка: {e}")
    elif cmd.startswith('moves'):
        # Команда: moves x2 y2
        parts = cmd.split()
        if len(parts) == 3:
            try:
                x2 = int(parts[1])
                y2 = int(parts[2])
                steps = turtle.count_moves(x2, y2)
                print(f"Минимальное количество шагов до ({x2}, {y2}): {steps}")
            except ValueError:
                print("Некорректные координаты. Введите целые числа.")
        else:
            print("Неверный формат. Введите: moves x2 y2")
    else:
        print("Неизвестная команда.")