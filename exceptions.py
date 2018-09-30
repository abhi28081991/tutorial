import math


def split_check(total, people):
    return math.ceil(total / people)

try:
    total_due = float(input("enter total amount"))
    no_of_person = int(input('enter person'))

except ZeroDivisionError:
    print("enter no of person more than 0")
except ValueError:
    print("please enter valid number")
else:
    amount_due = split_check(total_due, no_of_person)
    print(amount_due)
