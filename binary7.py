loop=1
while(loop):
    decide = int(input("Enter 1 to perform 1's Complement and 2 for 2's Complement: "))

    if decide == 1:
        loop=0
        num = input("Enter the binary number to perform 1's complement: ")

        for char in num:
            if char not in '01':
                print("Invalid input. Please enter a binary number.")
                break
        else:
            complement = ''.join('1' if char == '0' else '0' for char in num)
            print("1's complement is:", complement)

    elif decide == 2:
        loop=0
        num = input("Enter the binary number to perform 2's complement: ")

        for char in num:
            if char not in '01':
                print("Invalid input. Please enter a binary number.")
                break
        else:
            ones_complement = ''.join('1' if char == '0' else '0' for char in num)
        
            twos_complement = bin(int(ones_complement, 2) + 1)[2:]

            twos_complement = twos_complement.zfill(len(num))

            print("2's complement is:", twos_complement)

    else:
        loop=1
        print("Invalid choice. Please enter 1 or 2.")
