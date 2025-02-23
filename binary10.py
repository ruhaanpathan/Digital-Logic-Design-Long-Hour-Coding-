def find_15s_complement(hex_number):
    complement = ''.join(format(15 - int(digit, 16), 'X') if digit.isalnum() else '.' for digit in hex_number.upper())
    return complement

def find_16s_complement(hex_number):
    fifteen_complement = find_15s_complement(hex_number)

    if '.' in fifteen_complement:
        integer_part, fractional_part = fifteen_complement.split('.')
        integer_value = int(integer_part, 16) + 1  
        sixteen_complement = hex(integer_value)[2:].upper() + '.' + fractional_part 
    else:
        integer_value = int(fifteen_complement, 16) + 1 
        sixteen_complement = hex(integer_value)[2:].upper()

    return sixteen_complement

def main():
    hex_number = input("Enter a hexadecimal number (with or without decimal point): ").strip().upper()

    if not all(c in '0123456789ABCDEF.' for c in hex_number):
        print("Invalid hexadecimal number!")
        return

    fifteen_complement = find_15s_complement(hex_number)
    sixteen_complement = find_16s_complement(hex_number)

    print("15's Complement:", fifteen_complement)
    print("16's Complement:", sixteen_complement)

if __name__ == "__main__":
    main()
