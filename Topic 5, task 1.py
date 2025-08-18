num = int(input("Enter an integer: "))

if num == 0:
    print("zero number")
else:
    # Determine number's sign
    if num > 0:
        sign = "positive"
    else:
        sign = "negative"
    
    # Check parity
    if num % 2 == 0:
        parity = "even"
        print(f"{sign} {parity} number")
    else:
        print("number is not even")