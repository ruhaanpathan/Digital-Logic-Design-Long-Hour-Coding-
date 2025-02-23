def find_7s_complement(octal_number):
    complement = ''.join(str(7 - int(digit)) if digit.isdigit() else '.' for digit in octal_number)
    return complement

def find_8s_complement(octal_number):
    seven_complement = find_7s_complement(octal_number)
    
    if '.' in seven_complement:
        integer_part, fractional_part = seven_complement.split('.')
        integer_value = int(integer_part, 8) + 1 
        fractional_value = fractional_part  
        eight_complement = oct(integer_value)[2:] + '.' + fractional_value 
    else:
        integer_value = int(seven_complement, 8) + 1  
        eight_complement = oct(integer_value)[2:]  

    return eight_complement

def main():
    octal_number = input("Enter an octal number (with or without decimal point): ").strip()

    if not all(c in '01234567.' for c in octal_number):
        print("Invalid octal number!")
        return

    seven_complement = find_7s_complement(octal_number)
    eight_complement = find_8s_complement(octal_number)

    print("7's Complement:", seven_complement)
    print("8's Complement:", eight_complement)

if __name__ == "__main__":
    main()
