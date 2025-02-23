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

sys = input("Enter number system (binary, decimal, hexadecimal, octal, radix-r): ")
num = input("Enter the number: ")
print(next_binary(sys, num))