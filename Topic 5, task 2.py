word = input("Enter a word in lowercase Latin letters: ")

vowels = {'a', 'e', 'i', 'o', 'u'}
vowel_count = 0
consonant_count = 0
individual_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letter in word:
    if letter in vowels:
        vowel_count += 1
        individual_counts[letter] += 1
    else:
        consonant_count += 1

print(f"Total vowels: {vowel_count}")
print(f"Total consonants: {consonant_count}")

# Print individual vowel counts or False if not present
for vowel in sorted(individual_counts.keys()):
    count = individual_counts[vowel]
    if count == 0:
        print(f"{vowel}: False")
    else:
        print(f"{vowel}: {count}")