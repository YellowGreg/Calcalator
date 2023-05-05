import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    return math.sqrt(x)

def log(x, base):
    return math.log(x, base)

print('Welcome to the YellowGreg Stupid Calculator')

while True:
    print('Please select an operation:')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Power')
    print('6. Square root')
    print('7. Logarithm')
    print('0. Exit')

    choice = input('Enter your choice: ')

    if choice == '0':
        print('Thank you for using the calculator!')
        break

    if choice not in ['1', '2', '3', '4', '5', '6', '7',]:
        print('Invalid choice, please try again.')
        continue

    x = float(input('Enter the first number: '))
    if choice != '6':
        y = float(input('Enter the second number: '))

    if choice == '1':
        print(f'{x} + {y} = {add(x, y)}')
    elif choice == '2':
        print(f'{x} - {y} = {subtract(x, y)}')
    elif choice == '3':
        print(f'{x} * {y} = {multiply(x, y)}')
    elif choice == '4':
        try:
            print(f'{x} / {y} = {divide(x, y)}')
        except ValueError as e:
            print(str(e))
    elif choice == '5':
        print(f'{x} ^ {y} = {power(x, y)}')
    elif choice == '6':
        print(f'sqrt({x}) = {sqrt(x)}')
    elif choice == '7':
        base = float(input('Enter the base of the logarithm: '))
        print(f'log_{base}({x}) = {log(x, base)}')
