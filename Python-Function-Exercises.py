# 1. Write a Python function to find the Max of three numbers.
# def findthreemax(num1, num2, num3):
#     if num1 > num2:
#         if num1 > num3:
#             print(num1)
#     elif num2 > num1:
#         if num2 > num3:
#             print(num2)
#     elif num3 > num2:
#         if num3 > num1:
#             print(num3)
#
# findthreemax(8,3,6)

# 2. Write a Python function to sum all the numbers in a list.

# list = [2, 6, 4, 9, 10, 1]
#
# def sumnumbers():
#     sum = 0
#     for i in list:
#         sum = sum + i
#     print(sum)
# sumnumbers()

# 3. Write a Python function to multiply all the numbers in a list.

# list = [2, 6, 4, 9, 10, 1]
#
# def mulnumbers():
#     mul = 1
#     for i in list:
#         mul = mul * i
#     print(mul)
#
# mulnumbers()

# 4. Write a Python program to reverse a string.

# your_string = str(input("Enter String "))
#
# def reversestring():
#     space = [] * len(your_string)
#     for i in range(len(your_string)):
#         space.insert(0,your_string[-i])
#     string="".join(space)
#     print(string)

# reversestring()

'''5. Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.'''

# fact_number = int(input("Enter a number "))
#
# def factorial_number(fact_number):
#     factor_space = []
#     for i in range(1 ,fact_number + 1, 1):
#         factor_space.append(i)
#     factorial = 1
#     for x in factor_space:
#         factorial = factorial * x
#     print(factorial)
#
# factorial_number(fact_number)

#6.Write a Python function to check whether a number is in a given range.
#
# def range_number(small_number,number, big_number):
#     hello = True
#     while hello:
#         if number > small_number and number  < big_number:
#             hello = False
#             print("Your number " + str(number) + " is within range")
#         elif number < small_number or number > big_number:
#             print("Your number is not within range")
#             hello = False
#
# range_number(8,4,10)

''' 7. Write a Python function that accepts a string and calculate
 the number of upper case letters and lower case letters.'''

# string = str(input("Enter a String "))
#
# def uppercasecounter(string):
#     stored_number=[]
#     number_uppercase = 0
#     for i in string:
#         stored_number.append(i)
#
#     for x in range(len(string)):
#             if stored_number[x] == string.upper()[x]:
#                 number_uppercase += 1
#     print(number_uppercase)
# uppercasecounter(string)

'''8. Write a Python function that takes a list,
 then returns it and shuffles it into a new list.'''

# import random
#
# list = ["a", "b", "c", 1, 2, 3]
#
# def random_list():
#     shuffle_list = random.shuffle(list)
#     random_len = random.randint(1, len(list))
#     new_list=[]
#     for i in range(random_len):
#         new_list.append(list[i])
#     print(new_list)
#
# random_list()
'''9. Write a Python function that takes a number
 as a parameter and check the number is prime or not.'''

def main():
n = input("Please enter a number:")
is_prime(n)

def is_prime(a):
    x = True
    for i in (2, a):
            while x:
               if a%i == 0:
                   x = False
               else:
                   x = True


    if x:
        print "prime"
    else:
        print "not prime"

main()















