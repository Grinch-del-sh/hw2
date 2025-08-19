# Get input string and remove any leading/trailing whitespace
user_input = input("Enter a string (no spaces): ").strip()

# Check if string reads the same forwards and backwards
if user_input == user_input[::-1]:
    print("yes")
else:
    print("no")