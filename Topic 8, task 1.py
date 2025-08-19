# Input
N = int(input("Enter N: "))  # Number of elements
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(N)]

# Reverse and output
reversed_numbers = numbers[::-1]
print("Reversed array:")
print(' '.join(map(str, reversed_numbers)))