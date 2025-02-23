def next_binary(sys, num):
    try:
        if sys.lower() == "binary":
            base = 2
            next_num = bin(int(num, base) + 1)[2:]  
        elif sys.lower() == "decimal":
            base = 10
            next_num = str(int(num, base) + 1)
        elif sys.lower() == "hexadecimal":
            base = 16
            next_num = hex(int(num, base) + 1)[2:].upper()
        elif sys.lower() == "octal":
            base = 8
            next_num = oct(int(num, base) + 1)[2:]
        elif sys.lower().startswith("radix-"):
            base = int(sys.split("-")[1])
            if base < 2 or base > 36:
                return "Invalid radix (must be between 2 and 36)"
            next_num = format(int(num, base) + 1, f'X' if base == 16 else '')
        else:
            return "Invalid number system"

        return f"Next number in {sys}: {next_num}"
    except ValueError:
        return "Invalid number for the given system"
    
def is_valid_number(num_system, number):

    if num_system == 'binary':
        for char in number:
            if char not in '01.':
                return "Invalid"
        return "Valid"
    
    elif num_system == 'decimal':
        for char in number:
            if char not in '0123456789.':
                return "Invalid"
        return "Valid"
    
    elif num_system == 'hexadecimal':
        for char in number:
            if char not in '0123456789abcdefABCDEF.':
                return "Invalid"
        return "Valid"
    
    elif num_system == 'octal':
        for char in number:
            if char not in '01234567.':
                return "Invalid"
        return "Valid"
    
    elif num_system.startswith('radix-'):
        try:
            radix = int(num_system.split('-')[1])
            if 2 <= radix <= 36:
                valid_chars = '.0123456789abcdefghijklmnopqrstuvwxyz'[:radix]
                for char in number:
                    if char not in valid_chars:
                        return "Invalid"
                return "Valid"
            else:
                return "Invalid"
        except ValueError:
            return "Invalid"
    
    else:
        return "Invalid"


    
    
def convert_integer_to_base(num, base):
    if num == 0:
        return "0"
    
    digits = []
    while num > 0:
        remainder = num % base
        if remainder < 10:
            digits.append(str(remainder))
        else:
            digits.append(chr(remainder - 10 + ord('A')))
        num //= base
    
    return ''.join(digits[::-1])

def convert_fractional_to_base(num, base):
    fractional_result = []
    for _ in range(6):
        num *= base
        integer_part = int(num)
        if integer_part < 10:
            fractional_result.append(str(integer_part))
        else:
            fractional_result.append(chr(integer_part - 10 + ord('A')))
        num -= integer_part
        
        if num == 0:
            break
    
    return ''.join(fractional_result)

def convert_decimal_to_base(number, base, number_type):
    if number_type == 'i':
        integer_part = int(number)
        fractional_part = 0
        integer_result = convert_integer_to_base(integer_part, base)
        print(integer_result)
    
    elif number_type == 'f':
        integer_part = int(number)
        fractional_part = number - integer_part
        integer_result = convert_integer_to_base(integer_part, base)
        fractional_result = convert_fractional_to_base(fractional_part, base)
        print(f"{integer_result}.{fractional_result}")
    
    else:
        print("Invalid number type!")







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


    
def to_decimal(number, base):
    """Convert a number from any base to decimal."""
    try:
        if '.' in number:  # Fractional number
            integer_part, fractional_part = number.split('.')
            integer_value = int(integer_part, base)
            fractional_value = sum(int(digit, base) / (base ** (i + 1)) for i, digit in enumerate(fractional_part))
            return integer_value + fractional_value
        else:  # Integer number
            return int(number, base)
    except ValueError:
        print("Invalid number for the given base.")
        return None

def from_decimal(decimal_number, base, is_fractional=False):
    """Convert a decimal number to any given base."""
    if not is_fractional:
        return convert_integer_part(int(decimal_number), base)
    else:
        integer_part = int(decimal_number)
        fractional_part = decimal_number - integer_part
        return convert_integer_part(integer_part, base) + '.' + convert_fractional_part(fractional_part, base)

def convert_integer_part(integer_part, base):
    """Convert integer part of a number to any base."""
    if integer_part == 0:
        return '0'
    digits = []
    while integer_part:
        digits.append("0123456789ABCDEF"[integer_part % base])
        integer_part //= base
    return ''.join(digits[::-1])

def convert_fractional_part(fractional_part, base, precision=5):
    """Convert fractional part of a number to any base."""
    result = []
    while fractional_part > 0 and len(result) < precision:
        fractional_part *= base
        digit = int(fractional_part)
        result.append("0123456789ABCDEF"[digit])
        fractional_part -= digit
    return ''.join(result)

def get_base(system):
    """Get the numeric base for the given system."""
    if system == "binary":
        return 2
    elif system == "octal":
        return 8
    elif system == "hexadecimal":
        return 16
    elif system.startswith("radix-"):
        try:
            return int(system.split('-')[1])
        except ValueError:
            print("Invalid radix format. Use radix-r where r = 2^n.")
            return None
    else:
        print("Unsupported number system!")
        return None

def main():
    """Main function to get user input and convert the number."""
    input_system = input("Enter input number system (binary, octal, hexadecimal, radix-r where r=2^n): ").strip().lower()
    output_system = input("Enter output number system (binary, octal, hexadecimal, radix-r where r=2^n): ").strip().lower()
    number_type = input("Choose number type (integer/fractional): ").strip().lower()
    number = input("Enter the number: ").strip()

    input_base = get_base(input_system)
    output_base = get_base(output_system)

    if input_base is None or output_base is None:
        return

    is_fractional = '.' in number and number_type == "fractional"
    decimal_value = to_decimal(number, input_base)

    if decimal_value is None:
        return

    converted_number = from_decimal(decimal_value, output_base, is_fractional)
    print("Converted number:", converted_number)
choice =0
while(choice !=1 and choice!=2 and choice !=3 and choice!=4 and choice !=5):
    choice =int(input("Enter 1 for the next number in any given number system\nEnter 2 to identify the valid number of any given number system\nEnter 3 to Convert Decimal number in to any other number system\nEnter 4 to Convert any number of any number system to decimal number\nEnter 5 to Convert any number of any number system (octal, hexadecimal,2n) to any number system system (octal, hexadecimal, 2n)\nEnter Num here: "))
    if choice == 1:
        sys = input("Enter number system (binary, decimal, hexadecimal, octal, radix-r): ")
        num = input("Enter the number: ")
        print(next_binary(sys, num))
    elif choice == 2:
        num_system = input("Enter the number system (binary, decimal, hexadecimal, octal, radix-r): ").strip().lower()
        number = input("Enter the number: ").strip()
        print(is_valid_number(num_system, number)) 
    elif choice ==3:
        base = int(input("Enter the target number system (2 for binary, 8 for octal, 16 for hexadecimal, or any other number for custom base): "))
        number_type = input("Enter the number type (i for integer, f for fractional): ").strip().lower()
        number = float(input("Enter the decimal number: "))
        convert_decimal_to_base(number, base, number_type)
    elif choice ==4:
        number_system = input("Enter number system (binary, octal, hexadecimal, radix-r): ").strip().lower()
        number_type = input("Enter number type (integer/fractional): ").strip().lower()
        number = input(f"Enter the {number_system} number: ").strip()

        try:
            decimal_result = convert_to_decimal(number_system, number_type, number)
            print(f"The decimal representation of {number} is: {decimal_result}")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice==5:
        main()
    else:
        print("Enter valid number")