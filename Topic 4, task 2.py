number = int(input("Enter a 5-digit integer: "))

# Extract each digit place
ten_thousands = number // 10000
thousands = (number // 1000) % 10
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

# Perform calculations
step1 = tens ** units        # Raise tens to power of units
step2 = step1 * hundreds     # Multiply by hundreds
step3 = ten_thousands - thousands  # Difference of ten-thousands and thousands
result = step2 / step3       # Final division

print(f"Result: {result}")