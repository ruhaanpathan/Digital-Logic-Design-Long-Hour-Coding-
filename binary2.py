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

num_system = input("Enter the number system (binary, decimal, hexadecimal, octal, radix-r): ").strip().lower()
number = input("Enter the number: ").strip()
print(is_valid_number(num_system, number))