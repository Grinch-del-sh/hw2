numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
seen = set()
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)