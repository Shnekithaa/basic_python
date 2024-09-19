## Nested Conditional Statements

### Example Problem to check if the user is eligible to vote or not


unra_vayasu = int(input())
voter_ID_irukka = input()
if unra_vayasu:
    if voter_ID_irukka == "Yes":
        print("Vote panalam")
    else:
        print("VOTER_ID venum")
else:
    print("Vayasu pathala. Adutha election la try panunga!")


### Example Problem to print the greatest among the given two numbers


number_1 = int(input())
number_2 = int(input())
if number_1 > number_2:
    print(number_1)
else:
    if number_1 == number_2:
        print("Equal")
    else:
        print(number_2)