#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    last_digit = number % 10
    last_digit *= -1
    number *= -1
else:
    last_digit = number % 10
    
str = f"Last digit of {number:d}is {last_digit:d} "
if last_digit > 5:
    str+="and is greater than 5"
elif last_digit == 0:
    str+="and is 0"
elif last_digit < 6 and last_digit != 0:
    str+="and is less than 6 and not 0"
print(str)