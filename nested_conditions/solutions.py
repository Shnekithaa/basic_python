# Possible Solutions:
## 1)

number_1 = int(input())
number_2 = int(input())
if number_1 < number_2:
    print(number_1)
else:
    if number_1 == number_2:
        print("Equal")
    else:
        print(number_2)

## 2)

number = int(input())
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
else:
    print("The number is not positive")

## 3)

num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2 and num1 > num3:
    print(num1)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)
