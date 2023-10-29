# Add String - Ques 415

import sys

def addStrings(num1, num2):
    sys.set_int_max_str_digits(10000)
    number1 = int(num1)
    number2 = int(num2)
    add = str(number1 + number2)
    return add

""" TC 1"""
num1 = "11"
num2 = "123"
# # Output: "134"

""" TC 2"""
# num1 = "0"
# num2 = "0"
# # Output: "0"

""" TC 3 """
# num1 = "1"
# num2 = "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"

print(addStrings(num1, num2))