num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
for i in range(1,num1 and num2):
    if(num1%i==0 and num2%i==0):
        hcf=i
lcm=(num1*num2)//hcf
print("GCD of the num is",hcf)
print("LCM of the num is",lcm)

