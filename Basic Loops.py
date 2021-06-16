# Homework 5: Basic Loops

for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number == 2:
        print("Prime")
    elif number == 1:
        print(1)
    elif number == 7:
        print("Prime")
    elif number % 2 > 0 and number % 3 > 0 and number % 5 > 0 and number % 7 > 0:
        print("Prime")
    else:
        print(number)
