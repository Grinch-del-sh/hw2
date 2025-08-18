a, b = map(int, input("Enter A and B: ").split())

# Using list comprehension
evens = [str(num) for num in range(a, b + 1) if num % 2 == 0]
print(' '.join(evens))

# Alternative without list
# for num in range(a + (a % 2), b + 1, 2):
#     print(num, end=' ')