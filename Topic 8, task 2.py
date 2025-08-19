# Input
N = int(input("Enter N: "))
arr = list(map(int, input("Enter numbers (space-separated): ").split()))

# Reorder
if N > 1:
    modified_arr = [arr[-1]] + arr[:-1]
else:
    modified_arr = arr

# Output
print("Modified array:")
print(' '.join(map(str, modified_arr)))