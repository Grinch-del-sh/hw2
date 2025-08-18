X = int(input("Enter the minimum investment amount X: "))
A = int(input("How much does Michael have? "))
B = int(input("How much does Ivan have? "))

if A >= X and B >= X:
    print(2)
elif A >= X:
    print("Mike")
elif B >= X:
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)