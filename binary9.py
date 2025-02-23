def find_9s_complement(decimal_number):
    complement = ''.join(str(9 - int(digit)) if digit.isdigit() else '.' for digit in decimal_number)
    return complement

def find_10s_complement(decimal_number):
    nine_complement = find_9s_complement(decimal_number)
    
    if '.' in nine_complement:
        integer_part, fractional_part = nine_complement.split('.')
        integer_value = int(integer_part) + 1 
        ten_complement = str(integer_value) + '.' + fractional_part 
    else:
        integer_value = int(nine_complement) + 1 
        ten_complement = str(integer_value)

    return ten_complement

def main():
    decimal_number = input("Enter a decimal number (with or without decimal point): ").strip()

    if not all(c.isdigit() or c == '.' for c in decimal_number):
        print("Invalid decimal number!")
        return

    nine_complement = find_9s_complement(decimal_number)
    ten_complement = find_10s_complement(decimal_number)

    print("9's Complement:", nine_complement)
    print("10's Complement:", ten_complement)

if __name__ == "__main__":
    main()
