def add_function(num1, num2):
    return num1+num2


def sub_function(num1, num2):
    return num1-num2


def square_function(num1, num2):
    sq1 = num1**2
    sq2 = num2**2
    return sq1, sq2


def cube_function(num1, num2):
    cube1 = num1**3
    cube2 = num2**3
    return cube1, cube2


number1 = int(input("Enter a first number : "))
number2 = int(input("Enter a second number : "))
operator = input("Enter an operator : ")

# Using if-else statements to perform operations
if operator == '+':
    numbers_sum = add_function(number1, number2)
    print(f"{number1} + {number2} =",  numbers_sum)
elif operator == '-':
    numbers_sub = sub_function(number1, number2)
    print(f"{number1} - {number2} =",  numbers_sub)
elif operator == 's':
    sq1, sq2 = square_function(number1, number2)
    print(f"square of {number1} =", sq1)
    print(f"square of {number2} =", sq2)
elif operator == 'c':
    cube1, cube2 = cube_function(number1, number2)
    print(f"cube of {number1} =", cube1)
    print(f"cube of {number2} =", cube2)
else:
    print("Invalid operator (+, -, s, or c).")
