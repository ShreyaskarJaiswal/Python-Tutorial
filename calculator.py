import math

def addition(num1, num2):
	print( num1 + num2)

def subtraction(num1, num2):
	print( num1 - num2)

def multiplication(num1, num2):
	print( num1 * num2)

def division(num1, num2):
	print( num1 / num2)

def modulos(num1, num2):
	print( num1 % num2)

def power(num1, num2):
	print( num1 ** num2)

def integerDivision(num1, num2):
	print( num1 // num2)

def fact(num1):
    print(math.factorial(num1))

while True:
    print()
    
    ans =input("Want to use the calculator (Y or N)\n")
    
    if ans!='y'and ans!='Y':
        print("Exited...")
        break
        
    else:
        print("Choose the operation:")
        print("1. Addition(+)\n" "2. Subtraction(-)\n" "3. Multiplication(x)\n" "4. Division(/)\n"
              "5. Modulos(%)\n""6. Power(^)\n""7. Integer Division(//)\n""8. Factorial(!)\n")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            num_1 = int(input("Enter 1st number: "))
            num_2 = int(input("Enter 2nd number: "))
            addition(num_1,num_2)

        elif choice == 2:
            num_1 = int(input("Enter 1st number: "))
            num_2 = int(input("Enter 2nd number: "))
            subtraction(num_1, num_2)

        elif choice == 3:
            num_1 = int(input("Enter 1st number: "))
            num_2 = int(input("Enter 2nd number: "))
            multiplication(num_1, num_2)

        elif choice == 4:
            num_1 = int(input("Enter 1st number: "))
            num_2 = int(input("Enter 2nd number: "))
            division(num_1, num_2)

        elif choice == 5:
            num_1 = int(input("Enter 1st number: "))
            num_2 = int(input("Enter 2nd number: "))
            modulos(num_1, num_2)

        elif choice == 6:
            num_1 = int(input("Enter 1st number: "))
            num_2 = int(input("Enter 2nd number: "))
            power(num_1, num_2)

        elif choice == 7:
            num_1 = int(input("Enter 1st number: "))
            num_2 = int(input("Enter 2nd number: "))
            integerDivision(num_1, num_2)

        elif choice == 8:
            num = int(input("Enter the number: "))
            fact(num)

        else:
            print("Invalid input")
    
