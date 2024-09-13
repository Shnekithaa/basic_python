## Conditional Statements

### if else

unra_number = int(input())
if unra_number > 0:
    print("Positive Number")
else:
    print("Negative Number")


### if elif else


unra_marks = int(input())
if unra_marks > 80:
    print("Excellent")
elif unra_marks > 60 and unra_marks < 80:
    print("Good")
elif unra_marks > 35 and unra_marks < 60:
    print("Needs Improvement")
else:
    print("Poor")


### Example Problem to check if the user is eligible to vote or not


unra_vayasu = int(input())
if unra_vayasu >= 18:
    print("Vote panna ready")
else:
    print("Vote panna mudiyathu")