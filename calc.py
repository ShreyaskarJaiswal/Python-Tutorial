'''
1.addition
2.subtraction
3.multiply
4.division-q,r
5.exponent(power)
factorial
log
exp(e)
summation
square
square root
cube
'''

import math

def addition():
        num_1 = float(input("Enter 1st number: "))
        num_2 = float(input("Enter 2nd number: "))
        sum_= num_1 + num_2
        print(f"Sum of {num_1} and {num_2} is {sum_}")

def subtraction():
        num_1 = float(input("Enter 1st number: "))
        num_2 = float(input("Enter 2nd number: "))
        sub_= num_1-num_2
        print(f"Subtracting {num_1} from {num_2} is {sub_}")

def multiplication():
        num_1 = float(input("Enter 1st number: "))
        num_2 = float(input("Enter 2nd number: "))
        mul_= num_1*num_2
        print(f"Product of {num_1} and {num_2} is {mul_}")

	

def division():
        num_1 = float(input("Enter 1st number: "))
        num_2 = float(input("Enter 2nd number: "))
        quo_= num_1 / num_2
        rem = num_1 % num_2
        print(f"Quotient of {num_1} and {num_2} is {quo_}")
        print(f"Remainder of {num_1} and {num_2} is {rem}")

def power():
        num_1 = float(input("Enter 1st number: "))
        num_2 = float(input("Enter 2nd number: "))
        pow_ = num_1**num_2
        print(f"Power of {num_1} to the {num_2} is {pow_}")

def integerDivision():
        num_1 = float(input("Enter 1st number: "))
        num_2 = float(input("Enter 2nd number: "))
        pow_ = num_1//num_2
        print(f"Integer division of {num_1} by {num_2} is {pow_}")

def fact():
        num_1 = float(input("Enter the number: "))
        pow_ = math.factorial(num_1)
        print(f"Factorial of {num_1}  is {pow_}")

def exponent():
        num_1 = float(input("Enter the number: "))
        pow_ = math.exp(num_1)
        print(f"Exponent of {num_1}  is {pow_}")

def sq_root():
        num_1 = float(input("Enter the number: "))
        pow_ = math.sqrt(num_1)
        print(f"Square Root of {num_1}  is {pow_}")

def sqr():
        num_1 = float(input("Enter the number: "))
        pow_ = num_1*num_1
        print(f"Square of {num_1}  is {pow_}")

def cube():
        num_1 = float(input("Enter the number: "))
        pow_ = num_1*num_1*num_1
        print(f"Cube of {num_1}  is {pow_}")


def logarithm():
        num_1 = float(input("Enter the number: "))
        pow_ = math.log(num_1)
        print(f"Log of {num_1}  is {pow_}")

def summation():
        sum_=0
        num_1 = int(input("Enter the number: "))
        for i in range(num_1+1):
                sum_=sum_+i
        print("Summation of ",sum_)
         


