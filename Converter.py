'''
Binary to Decimal and Decimal to Binary Converter by Ivan
'''

print("Which conversion do you choose: ")
print("1. Decimal to Binary ")
print("2. Binary to Decimal ")

choices = [1, 2]

while True:
    while True:
        try:
            choice = int(input("Select 1 or 2 "))
            break
        except ValueError:
            print("Please enter a numerical value: ")
            continue

    if choice == 1:
        binary_num = list(input("Input a binary number: "))
        value = 0

        for i in range(len(binary_num)):
            digit = binary_num.pop()
            if digit == '1':
                value = value + pow(2, i)
        print("The decimal value of the binary list is", value)
    elif choice == 2:
        while True:
            try:
                num = int(input("Please enter a number you wish to convert: "))
                break
            except ValueError:
                print("Please enter a numerical value: ")
                continue
        print(f'The binary representation of {num} is {bin(num)}')

    again = input("Do you wish to perform another conversion? (Y/N) ").upper()

    if again[0] == 'Y':
        continue
    else:
        break
