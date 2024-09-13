# Possible Solutions:
## 1)

number_1 = int(input())
number_2 = int(input())
if number_1 > number_2:
    print(number_1)
else:
    print(number_2)

## 2)

number = int(input())
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")

## 3)

given_number = int(input())
if given_number % 2 == 0:
    print("Even")
else:
    print("Odd")