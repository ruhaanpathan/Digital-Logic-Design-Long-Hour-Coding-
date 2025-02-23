def find_7s_complement(octal_number):
    """Find the 7's complement of an octal number."""
    complement = ''.join(str(7 - int(digit)) if digit.isdigit() else '.' for digit in octal_number)
    return complement

def find_8s_complement(octal_number):
    """Find the 8's complement by adding 1 to the 7's complement."""
    seven_complement = find_7s_complement(octal_number)
    
    # Handle integer and fractional parts separately
    if '.' in seven_complement:
        integer_part, fractional_part = seven_complement.split('.')
        integer_value = int(integer_part, 8) + 1  # Add 1 to integer part only
        fractional_value = fractional_part  # Keep fractional part unchanged
        eight_complement = oct(integer_value)[2:] + '.' + fractional_value  # Convert integer part back to octal
    else:
        integer_value = int(seven_complement, 8) + 1  # Add 1 to integer
        eight_complement = oct(integer_value)[2:]  # Convert back to octal

    return eight_complement

def main():
    """Main function to handle input and output."""
    octal_number = input("Enter an octal number (with or without decimal point): ").strip()

    # Validate input (should contain only octal digits and optionally a decimal point)
    if not all(c in '01234567.' for c in octal_number):
        print("Invalid octal number!")
        return

    seven_complement = find_7s_complement(octal_number)
    eight_complement = find_8s_complement(octal_number)

    print("7's Complement:", seven_complement)
    print("8's Complement:", eight_complement)

if __name__ == "__main__":
    main()
