# Класс Касса (CashRegister)
class CashRegister:
    def __init__(self):
        # Начальная сумма в кассе (можно задать через ввод, но по умолчанию 0)
        self.balance = 0

    def top_up(self, amount):
        """
        Пополняет кассу на указанную сумму.
        """
        self.balance += amount
        print(f"Касса пополнена на {amount}. Текущий баланс: {self.balance}")

    def count_1000(self):
        """
        Возвращает количество целых тысяч в кассе.
        """
        thousands = self.balance // 1000
        print(f"В кассе {thousands} целых тысяч.")
        return thousands

    def take_away(self, amount):
        """
        Забирает указанную сумму из кассы.
        Если денег недостаточно, выбрасывает ошибку ValueError.
        """
        if amount > self.balance:
            raise ValueError(f"Недостаточно денег в кассе! Требуется {amount}, доступно {self.balance}.")
        self.balance -= amount
        print(f"Из кассы забрали {amount}. Остаток: {self.balance}")


# ------------------------------------------------------------
# Основная программа для демонстрации работы класса
# ------------------------------------------------------------

# Создаём объект кассы
cashier = CashRegister()

print("Добро пожаловать в кассу!")
print("Доступные команды: top_up, count_1000, take_away, stop")

while True:
    command = input("\nВведите команду: ").strip().lower()
    if command == 'stop':
        print("Работа завершена.")
        break
    elif command == 'top_up':
        try:
            x = int(input("Введите сумму для пополнения: "))
            cashier.top_up(x)
        except ValueError:
            print("Ошибка: введите целое число.")
    elif command == 'count_1000':
        cashier.count_1000()
    elif command == 'take_away':
        try:
            x = int(input("Введите сумму для изъятия: "))
            cashier.take_away(x)
        except ValueError as e:
            print(f"Ошибка: {e}")
    else:
        print("Неизвестная команда. Попробуйте снова.")