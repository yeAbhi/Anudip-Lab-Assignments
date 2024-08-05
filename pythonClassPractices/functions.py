# 1. Function without Parameters
def greet():
    print("Hello, World!")

# 2. Function with Parameter
def greet_person(name):
    print(f"Hello, {name}!")

# 3. Function with Default Parameter
def greet_with_default(name="Stranger"):
    print(f"Hello, {name}!")

# 4. Function with Return Keyword
def add(a, b):
    return a + b

# Calling the functions to demonstrate them

# Function without Parameters
greet()  # Output: Hello, World!

# Function with Parameter
greet_person("Alice")  # Output: Hello, Alice!

# Function with Default Parameter
greet_with_default()  # Output: Hello, Stranger!
greet_with_default("Bob")  # Output: Hello, Bob!

# Function with Return Keyword
result = add(3, 5)
print(f"The sum is: {result}")  # Output: The sum is: 8






# # Recursion:

#           a) WAP to print factorial value of a given number using recursion.


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Test the function
# number = 5
# print(f"The factorial of {number} is {factorial(number)}")




#           b) WAP to display Fibonacci series up to 10 iteration using recursion.

# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fibs = fibonacci(n - 1)
#         fibs.append(fibs[-1] + fibs[-2])
#         return fibs

# # Display the Fibonacci series up to 10 iterations
# iterations = 10
# fib_series = fibonacci(iterations)
# print(f"Fibonacci series up to {iterations} iterations: {fib_series}")



