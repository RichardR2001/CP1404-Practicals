"""
Practical 4 - List Exercises
Created on 3/12/2021 by Richard Reynard
"""

# Basic list operations
numbers = []
number_count = 1
for i in range(1, 6):
    user_number = int(input(f"Number {number_count}: "))
    numbers.append(user_number)
    number_count = number_count + 1
print(f"The first number is:", numbers[0])
print(f"The last number is:", numbers[-1])
print(f"The smallest number is:", min(numbers))
print(f"The largest number is:", max(numbers))
average_number = sum(numbers)/len(numbers)
print("The average of the numbers is", average_number)


# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_username = input("Please input your username: ")
if user_username in usernames:
    print("Access granted")
else:
    print("Access denied")
