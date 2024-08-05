# 1. WAP to take a list print all the prime number available in list?
# list = [3,4,5,6,7,8,9]
# Output: 3, 5, 7

prime = []
list = [3,4,5,6,7,8,9, 12,34,56,78]
for number in list:
    if number == 2:
        prime.append(number)
    else:
        flag = True
        for i in range(2,number):
            if number % i == 0:
                flag=False
                break

        if flag==True:
            prime.append(number)


print(f"Total primes: {(prime)}")



# 2. WAP to take a list print count of all prime number available in list?
# list = [3,4,5,6,7,8,9, 12,34,56,78]

# prime = []
# list = [3,4,5,6,7,8,9,12,34,56,78]
# for number in list:
#     if number == 2:
#         prime.append(number)
#     else:
#         flag = True
#         for i in range(2,number):
#             if number % i == 0:
#                 flag=False
#                 break

#         if flag==True:
#             prime.append(number)


# print(f"Total primes: {len(prime)}")



# 3. WAP to take a list and print count of all even and odd numbers available in list?
# list = [3,4,5,6,7,8,9, 12,34,56,78]


# list = [3,4,5,6,7,8,9,12,34,56,78]

# even= 0
# odd = 0

# for n in range(len(list)):
#     if list[n] % 2 == 0:
        
#         even +=1
#     else:
        
#         odd +=1
# print("count of even numbers is" , even )
# print("count of odd numbers is" , odd )



