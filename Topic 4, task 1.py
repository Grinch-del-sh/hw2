# Get rectangle sides from user
try:
    a = float(input("Enter the first side length: "))
    b = float(input("Enter the second side length: "))
    
    # Validate positive values
    if a <= 0 or b <= 0:
        print("Error: sides must be positive numbers")
    else:
        # Calculate area and perimeter
        area = a * b
        perimeter = 2 * (a + b)
        
        # Display results
        print(f"Rectangle area: {area}")
        print(f"Rectangle perimeter: {perimeter}")
        
except ValueError:
    print("Error: please enter numeric values for sides")