# Импортируем collections для получения последнего ключа
import collections

# База данных питомцев (изначально пустая)
pets = {}

# ------------------------------------------------------------
# Вспомогательные функции
# ------------------------------------------------------------


def get_pet(pet_id):
    """
    Возвращает словарь с информацией о питомце по его ID,
    либо False, если питомец не найден.
    """
    return pets[pet_id] if pet_id in pets else False


def get_suffix(age):
    """
    Возвращает правильное склонение слова "год" для русского языка.
    """
    if 11 <= age % 100 <= 14:
        return "лет"
    if age % 10 == 1:
        return "год"
    if 2 <= age % 10 <= 4:
        return "года"
    return "лет"


def pets_list():
    """
    Выводит список всех питомцев с их ID.
    """
    if not pets:
        print("База данных пуста.")
        return
    print("\nСписок всех питомцев:")
    for pet_id, pet_data in pets.items():
        # pet_data = { "Имя": { "Вид": ..., "Возраст": ..., "Владелец": ... } }
        name = list(pet_data.keys())[0]
        info = pet_data[name]
        print(
            f"ID: {pet_id} - {name} ({info['Вид питомца']}, {info['Возраст питомца']} лет, владелец: {info['Имя владельца']})")


# ------------------------------------------------------------
# Основные CRUD-функции
# ------------------------------------------------------------

def create():
    """
    Создаёт новую запись о питомце и добавляет её в словарь pets.
    Новый ID = максимальный существующий ID + 1 (или 1, если база пуста).
    """
    # Определяем следующий ID
    if pets:
        last_id = collections.deque(pets, maxlen=1)[0]
        new_id = last_id + 1
    else:
        new_id = 1

    # Запрашиваем данные у пользователя
    name = input("Введите имя питомца: ")
    species = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    # Формируем структуру записи
    pet_info = {
        name: {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    pets[new_id] = pet_info
    print(f"Запись с ID {new_id} успешно создана.")


def read():
    """
    Читает и выводит информацию о питомце по его ID.
    """
    pet_id = int(input("Введите ID питомца: "))
    pet_data = get_pet(pet_id)
    if pet_data is False:
        print("Питомец с таким ID не найден.")
        return

    # Извлекаем имя и информацию
    name = list(pet_data.keys())[0]
    info = pet_data[name]
    species = info["Вид питомца"]
    age = info["Возраст питомца"]
    owner = info["Имя владельца"]

    # Формируем вывод с правильным склонением
    suffix = get_suffix(age)
    print(
        f'Это {species} по кличке "{name}". Возраст питомца: {age} {suffix}. Имя владельца: {owner}')


def update():
    """
    Обновляет информацию о питомце по его ID.
    """
    pet_id = int(input("Введите ID питомца для обновления: "))
    pet_data = get_pet(pet_id)
    if pet_data is False:
        print("Питомец с таким ID не найден.")
        return

    # Получаем текущие данные
    name = list(pet_data.keys())[0]
    info = pet_data[name]

    print(
        f"Текущие данные: {name} ({info['Вид питомца']}, {info['Возраст питомца']} лет, владелец: {info['Имя владельца']})")
    print("Оставьте поле пустым, если не хотите его менять.")

    new_name = input(f"Новое имя (было '{name}'): ") or name
    new_species = input(
        f"Новый вид (был '{info['Вид питомца']}'): ") or info["Вид питомца"]
    new_age_input = input(f"Новый возраст (был {info['Возраст питомца']}): ")
    new_age = int(new_age_input) if new_age_input else info["Возраст питомца"]
    new_owner = input(
        f"Новый владелец (был '{info['Имя владельца']}'): ") or info["Имя владельца"]

    # Если имя изменилось, удаляем старый ключ и добавляем новый
    if new_name != name:
        # Сохраняем остальные данные
        pet_data[new_name] = {
            "Вид питомца": new_species,
            "Возраст питомца": new_age,
            "Имя владельца": new_owner
        }
        del pet_data[name]
    else:
        # Обновляем существующую запись
        info["Вид питомца"] = new_species
        info["Возраст питомца"] = new_age
        info["Имя владельца"] = new_owner

    print(f"Запись с ID {pet_id} успешно обновлена.")


def delete():
    """
    Удаляет запись о питомце по его ID.
    """
    pet_id = int(input("Введите ID питомца для удаления: "))
    pet_data = get_pet(pet_id)
    if pet_data is False:
        print("Питомец с таким ID не найден.")
        return

    # Подтверждение удаления
    confirm = input(
        f"Вы действительно хотите удалить запись с ID {pet_id}? (y/n): ").lower()
    if confirm == 'y':
        del pets[pet_id]
        print(f"Запись с ID {pet_id} удалена.")
    else:
        print("Удаление отменено.")


# ------------------------------------------------------------
# Основной цикл программы
# ------------------------------------------------------------

print("Добро пожаловать в базу данных ветеринарной клиники!")
print("Доступные команды: create, read, update, delete, list, stop")

while True:
    command = input("\nВведите команду: ").strip().lower()

    if command == 'stop':
        print("Работа завершена.")
        break
    elif command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'list':
        pets_list()
    else:
        print("Неизвестная команда. Попробуйте снова.")
