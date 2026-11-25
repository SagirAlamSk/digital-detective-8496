# A simple decimal to binary and hexadecimal converter

print("Welcome to the Number Converter!")

try:
    number = int(input("Enter a positive decimal number: "))

    if number < 0:
        print("Please enter a positive number.")
    else:
        binary_value = bin(number)
        hexadecimal_value = hex(number)

        print("Decimal:", number)
        print("Binary:", binary_value)
        print("Hexadecimal:", hexadecimal_value)

except ValueError:
    print("Invalid input. Please enter a whole number.")
