x = int(input("Enter X: "))
divisors = 0

for i in range(1, int(x**0.5) + 1):
    if x % i == 0:
        if x // i == i:
            divisors += 1
        else:
            divisors += 2

print(f"Number of divisors: {divisors}")