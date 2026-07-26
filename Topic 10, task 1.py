#Создаём пустой словарь
pets = {}

#Запрашиваем данные у пользователя
pet_name = input("Enter pet name: ")
pet_type = input("Enter pet type: ")
pet_age = int(input("Enter pet age: "))
owner_name = input("Enter owner name: ")

#Заполняем словарь
pets[pet_name] = {
    "type": pet_type,
    "age": pet_age,
    "owner": owner_name
}

#Функция для выбора правильного слова "year" (единственное / множественное число)
def age_word(n):
    return "year" if n == 1 else "years"

#Извлекаем данные с помощью keys() и values()
pet_names = list(pets.keys())
pet_infos = list(pets.values())

name = pet_names[0]
info = pet_infos[0]

species = info["type"]
age = info["age"]
owner = info["owner"]

#Итоговая строка
result = f'This is a {species} named "{name}". Pet age: {age} {age_word(age)}. Owner: {owner}'

print(result)