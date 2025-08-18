# Request pet information from user
pet_type = input("Enter pet species/type: ")
pet_name = input("Enter pet name: ")
pet_age = int(input("Enter pet age: "))

# Determine correct age suffix
if pet_age == 1:
    age_word = "year"
else:
    age_word = "years"

# Format and display the output
print(f'This is a {pet_type} named "{pet_name}". Age: {pet_age} {age_word}.')