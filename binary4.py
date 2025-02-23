def convert_to_decimal(number_system, number_type, number):
    number = number.strip().lower()
    
    if number_system == "binary":
        base = 2
    elif number_system == "octal":
        base = 8
    elif number_system == "hexadecimal":
        base = 16
    elif number_system.startswith("radix"):
        base = int(number_system.split('-')[1])  
    else:
        raise ValueError("Invalid number system")

    if number_type == "integer":
        
        decimal_value = int(number, base)
        return decimal_value
    elif number_type == "fractional":
        
        if '.' in number:
            integer_part, fractional_part = number.split('.')
        else:
            integer_part, fractional_part = number, ''
        
        integer_decimal = int(integer_part, base)
        
        fractional_decimal = 0
        for i, digit in enumerate(fractional_part):
            fractional_decimal += int(digit, base) * (base ** -(i + 1))

        return integer_decimal + fractional_decimal
    else:
        raise ValueError("Invalid number type")

number_system = input("Enter number system (binary, octal, hexadecimal, radix-r): ").strip().lower()
number_type = input("Enter number type (integer/fractional): ").strip().lower()
number = input(f"Enter the {number_system} number: ").strip()

try:
    decimal_result = convert_to_decimal(number_system, number_type, number)
    print(f"The decimal representation of {number} is: {decimal_result}")
except ValueError as e:
    print(f"Error: {e}")
