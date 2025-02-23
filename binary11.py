def find_r_minus_1_complement(radix, number):
    r_minus_1 = radix - 1
    complement = ''
    
    for digit in number:
        if digit.isdigit():  
            complement += str(r_minus_1 - int(digit))
        elif 'A' <= digit <= 'Z':  
            complement += format(r_minus_1 - (ord(digit) - ord('A') + 10), 'X')
        elif digit == '.':  
            complement += '.'
    
    return complement

def find_r_complement(radix, number):
    r_minus_1_complement = find_r_minus_1_complement(radix, number)

   
    if number.count('.') > 1:
        raise ValueError("Invalid number format: multiple decimal points.")

    if '.' in r_minus_1_complement:
        integer_part, fractional_part = r_minus_1_complement.split('.')
        integer_value = int(integer_part, radix) + 1  
        r_complement = format(integer_value, 'X' if radix > 10 else 'd') + '.' + fractional_part
    else:
        integer_value = int(r_minus_1_complement, radix) + 1 
        r_complement = format(integer_value, 'X' if radix > 10 else 'd')

    return r_complement

def main():
    try:
        radix = int(input("Enter the radix (base) of the number (base>=2 and base<=36): "))
        if not (2 <= radix <= 36):
            print("Invalid radix! Please enter a base between 2 and 36.")
            return

        number = input("Enter a radix-r number (with or without decimal point): ").strip().upper()

        valid_chars = set('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:radix] + '.')
        if not all(c in valid_chars for c in number):
            print(f"Invalid number for base {radix}!")
            return

        r_minus_1_complement = find_r_minus_1_complement(radix, number)
        r_complement = find_r_complement(radix, number)

        print(f"({radix-1})'s Complement:", r_minus_1_complement)
        print(f"{radix}'s Complement:", r_complement)

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
