#Abhinandan Kumar
#Student id - AF0411617


#Q1 Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# # Example usage:
# number = int(input("Enter a number: "))
# result = check_even_odd(number)
# print(result)

# OUTPUT
# Enter a number: 7
# Odd


#Q2 Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

# def check_voter_eligibility(age):
#     if age >= 18:
#         return "Eligible to vote"
#     else:
#         return "Not eligible to vote"

# # Example usage:
# age = int(input("Enter your age: "))
# result = check_voter_eligibility(age)
# print(result)


#OUTPUT
# Enter your age: 4
# Not eligible to vote



#Q3 Write a Python program that determines if a given year is a leap year or not.

# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# # Example usage:
# year = int(input("Enter a year: "))
# if is_leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

#OUTPUT
# Enter a year: 1900
# 1900 is not a leap year.


#Q4 Create a Python program that checks if a user-given number is positive, negative, or zero

# def check_number(number):
#     if number > 0:
#         return "Positive"
#     elif number < 0:
#         return "Negative"
#     else:
#         return "Zero"

# # Example usage:
# number = float(input("Enter a number: "))
# result = check_number(number)
# print(result)

#OUTPUT
# Enter a number: 6
# Positive

#Q5 Write a Python program that determines the largest of three numbers entered by the user.

# def find_largest(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# # Example usage:
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# largest = find_largest(num1, num2, num3)
# print(f"The largest number is {largest}.")

# OUTPUT
# Enter the first number: 5
# Enter the second number: 4
# Enter the third number: 3
# The largest number is 5.0.