numbers = []  # Initializing empty list

for i in range(10):  # Input from a user
    num = int(input("Enter an integer: "))
    numbers.append(num)

# To check whether numbers in given list are even or odd
for num in numbers:
    if num % 2 == 0:
        print("%d is even." % num)
    else:
        print("%d is odd." % num)