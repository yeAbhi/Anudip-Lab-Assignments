# def day_of_week(day):
#   match day:
#     case "Monday":
#       print("It's Monday, the start of the week!")
#     case "Tuesday":
#       print("It's Tuesday, hump day is approaching!")
#     case "Wednesday":
#       print("It's Wednesday, hump day!")
#     case "Thursday":
#       print("It's Thursday, almost there!")
#     case "Friday":
#       print("It's Friday, weekend is here!")
#     case "Saturday" | "Sunday":
#       print("It's the weekend!")
#     case _:
#       print("Invalid day")

# day_of_week("Sunday")


# day = int(input('Enter 1 for Monday \nEnter 2 for Tuesday \nEnter 3 for Wednesday\nEnter 4 for Thursday \nEnter 5 for Friday \nEnter 6 for Saturday&sunday   '))

# match day:
#     case 1:
#         print("It's Monday, the start of the week!")
#     case 2:
#         print("It's Tuesday, hump day is approaching!")
#     case 3:
#         print("It's Wednesday, hump day!")
#     case 4:
#         print("It's Thursday, almost there!")
#     case 5:
#         print("It's Friday, weekend is here!")
#     case 6:
#         print("It's the weekend!")
#     case _:
#         print('This is default case or invalid option')


# n = int(input("Enter the number of terms: "))
# a, b = 0, 1

# if n <= 0:
#   print("Please enter a positive integer")
# elif n == 1:
#   print(a)
# else:
#   print(a, b, end=" ")
#   for i in range(2, n):
#     c = a + b
#     print(c, end=" ")
#     a = b
#     b = c

# n = int(input("Enter the number:  "))
# for i in range(1, 11, 1):
#      c= n*i
#      print(c, end= ' ')

n = int(input("Enter a number: "))

for i in range(1,n+1,1):
    for j in range(1,i):
        print(j, end=' ')
    print(i)


for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j, end=' ')
    print()