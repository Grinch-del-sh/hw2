print("Enter first list (one number per line, empty line to finish):")
list1 = []
while True:
    num = input()
    if num == '':
        break
    list1.append(int(num))

print("Enter second list (one number per line, empty line to finish):")
list2 = []
while True:
    num = input()
    if num == '':
        break
    list2.append(int(num))

common = len(set(list1) & set(list2))
print(f"Number of common elements: {common}")