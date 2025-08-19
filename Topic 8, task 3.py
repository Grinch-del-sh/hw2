# Input
m = int(input("Boat weight limit (kg): "))
n = int(input("Number of fishermen: "))
weights = [int(input(f"Fisherman {i+1} weight (kg): ")) for i in range(n)]

# Calculate boats
weights.sort()
left, right = 0, n-1
boats = 0

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1
    right -= 1
    boats += 1

# Output
print(f"Minimum boats needed: {boats}")