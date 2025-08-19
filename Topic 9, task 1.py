n = int(input("Enter N: "))
numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
distinct_count = len(set(numbers))
print(f"Number of distinct numbers: {distinct_count}")