# Abhinandan Kumar
# Student id - AF0411617 
# ----------------------------------------------------------------------



# Q.1 Write a program for arithmetic operators


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))

# print(f"Addition: {num1+num2}")
# print(f"Subtraction: {num1-num2}")
# print(f"Multiplication: {num1*num2}")
# print(f"Division: {num1/num2}")
# print(f"Remainder: {num1-num2}")
# print(f"Floor Division: {num1//num2}")
# print(f"Exponentiaion: {num1**num2}")

#OUTPUT
# Enter a number: 2
# Enter a number: 5
# Addition: 7
# Subtraction: -3
# Multiplication: 10
# Division: 0.4
# Remainder: -3
# Floor Division: 0
# Exponentiaion: 32


# ----------------------------------------------------------------------



# Q.2 Write a program for assignment operators


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))

# result = num1 + num2
# print(f"Result variable is assigned the sum of {num1} and {num2} which is {result}")

#OUTPUT
# Enter a number: 4
# Enter a number: 3
# Result variable is assigned the sum of 4 and 3 which is 7

# ----------------------------------------------------------------------


# Q.3Write a program for Bitwise operators 

# a = 12
# b = 4

# print("Bitwise AND", a & b)
# print("Bitwise OR", a | b)
# print("Bitwise NOT negation of A", ~a)
# print("Bitwise XOR", a ^ b)
# print("Bitwise Right shift", a >> b)
# print("Bitwise Left shift", a << b)

#OUTPUT
# Bitwise AND 4
# Bitwise OR 12
# Bitwise NOT negation of A -13
# Bitwise XOR 8
# Bitwise Right shift 0
# Bitwise Left shift 192
# ----------------------------------------------------------------------



# Q.4 Write a program to calculate greatest of three numbers.

# def find_greatest(num1, num2, num3):
  

#   if num1 == num2 == num3:
#     return "All three numbers are equal."
#   elif (num1 == num2 and num1 != num3) or (num1 == num3 and num1 != num2) or (num2 == num3 and num2 != num1):
#     return "Two numbers are equal and one is largest."
#   elif num1 >= num2 and num1 >= num3:
#     return f"{num1} is the greatest."
#   elif num2 >= num1 and num2 >= num3:
#     return f"{num2} is the greatest."
#   else:
#     return f"{num3} is the greatest."

# # Get input from the user
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# # Call the function and print the result
# result = find_greatest(num1, num2, num3)
# print(result)




#OUTPUT
# Enter the first number: 2
# Enter the second number: 5
# Enter the third number: 7
# 7 is the greatest.



# ----------------------------------------------------------------------



# 1.      Calculate the area of a circle.

# pi = 3.14


# radius = float(input("Input a valid radius: "))
# area = pi * radius * radius
# print(f"Area of circle with given radius {radius} is {area}")

#OUTPUT
# Input a valid radius: 6
# Area of circle with given radius 6.0 is 113.03999999999999


# ----------------------------------------------------------------------



# 2.      Calculate the area of a triangle.


# base = float(input("Enter a valid base value: "))
# height = float(input("Enter a valid height value: "))

# # {}
# area = .5 * base * height
# print(f"Area of the given triangle is {round(area, 3)}")

#OUTPUT
# Enter a valid base value: 8
# Enter a valid height value: 4
# Area of the given triangle is 16.0


# ----------------------------------------------------------------------



# 3.      Calculate the area of a rectangle.


# length = float(input("Enter the length: "))
# breadth = float(input("Enter the breadth: "))

# area = length * breadth
# print(f"Area of the given rectangle is {round(area, 3)}")

#OUTPUT
# Enter the length: 4
# Enter the breadth: 7
# Area of the given rectangle is 28.0


# ----------------------------------------------------------------------


# 4.  Calculate the area of a square.


# side = float(input("Enter the side length: "))

# area = side * side
# print(f"Area of the given square is {round(area, 3)}")

#OUTPUT
# Enter the side length: 4
# Area of the given square is 16.0








