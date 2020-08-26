'''
A simple Calculator created by Ivan
'''


def add(x, y):
    sum = x + y

    return sum


def subtract(x, y):
    diff = x - y

    return diff


def multiply(x, y):
    mult = x * y

    return mult


def divide(x, y):
    div = x / y

    return div


def exponentiate(x, y):
    exp = x**y

    return exp


print("Hello. This is a simple calculator that can take two numbers and perform a couple of mathematical functions.")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. To the power of: ")

choice = ""
choices = [1, 2, 3, 4, 5]
while choice not in choices:
    choice = int(
        input("Select an operation from the following options (1-5): "))


while True:
    if choice in choices:

        while True:
            try:
                first = int(input("Please enter the first number: "))

                break
            except ValueError:
                print("Please enter a numerical value\n")
                continue

        while True:
            try:

                second = int(input("Please enter the second number: "))
                break
            except ValueError:
                print("Please enter a numerical value\n")
                continue

        if choice == 1:
            print(f"The sum of {first} and {second} is {add(first,second)}")
        elif choice == 2:
            print(
                f"The difference of {first} and {second} is {subtract(first,second)}")
        elif choice == 3:
            print(
                f"The product of {first} and {second} is {multiply(first,second)}")
        elif choice == 4:
            print(
                f"The quotient of {first} and {second} is {divide(first,second)}")
        else:
            print(
                f"The exponential result of {first} to the {second} power is {exponentiate(first,second)}")

    again = input("Do you want to calculate another problem? (Y/N) ").upper()
    if again[0] == "Y":
        continue
    else:
        break
