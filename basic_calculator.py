from tkinter.tix import Y_REGION
import calc as c


print("-------------------Welcome to my Calculator----------------")
print()
print("To use the calculator follow the instruction as follows:")
print("1. Addition(+)\t""2. Subtraction(-)\t" "3. Multiplication(x)\t""4. Division(/)")
print("5. Power(^)\t" "6. IntegerDivision(//)\t""7. Factorial(!)\t\t""8. Exponents(e)")
print("9. Log(log)\t"  "10. Square root()\t""11. Square\t\t""12. Cube\n""13. Summation")

while True:
    print()
    
    ans =input("Want to use the calculator (Y or N)\n")
    
    if ans!='y'and ans!='Y':
        print("---------Thanks for using Our Calculator----------")
        break
        
    else:
        
        choice = int(input("Enter your choice:"))

        if choice == 1:

            c.addition()

        elif choice == 2:

            c.subtraction()

        elif choice == 3:
            
            c.multiplication()

        elif choice == 4:

            c.division()


        elif choice == 5:
            
            c.power()

        elif choice == 6:
           
            c.integerDivision()

        elif choice == 7:
      
            c.fact()

        elif choice == 8:
            
            c.exponent()

        elif choice == 9:
            
            c.logarithm()
            
        elif choice == 10:
            
            c.sq_root()

        elif choice == 11:

            c.sqr()
        
        elif choice == 12:
            
            c.cube()
            
        elif choice == 13:

            c.summation()
        
        else:
            print("Invalid input")
    
