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

if __name__ == "__main__":
    base = int(input("Enter the target number system (2 for binary, 8 for octal, 16 for hexadecimal, or any other number for custom base): "))
    number_type = input("Enter the number type (i for integer, f for fractional): ").strip().lower()
    number = float(input("Enter the decimal number: "))
    
    convert_decimal_to_base(number, base, number_type)
