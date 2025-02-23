def to_decimal(number, base):
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
    if not is_fractional:
        return convert_integer_part(int(decimal_number), base)
    else:
        integer_part = int(decimal_number)
        fractional_part = decimal_number - integer_part
        return convert_integer_part(integer_part, base) + '.' + convert_fractional_part(fractional_part, base)

def convert_integer_part(integer_part, base):
    if integer_part == 0:
        return '0'
    digits = []
    while integer_part:
        digits.append("0123456789ABCDEF"[integer_part % base])
        integer_part //= base
    return ''.join(digits[::-1])

def convert_fractional_part(fractional_part, base, precision=5):
    result = []
    while fractional_part > 0 and len(result) < precision:
        fractional_part *= base
        digit = int(fractional_part)
        result.append("0123456789ABCDEF"[digit])
        fractional_part -= digit
    return ''.join(result)

def get_base(system):
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

if __name__ == "__main__":
    main()
