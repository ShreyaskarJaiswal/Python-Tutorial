print()
print("--------------------User Defined Function------------------------")
print()
def ourPrint(name,msg="Hi"):
    print(msg,name)

name=input("Enter Name")
ourPrint("Good Morning",name)
ourPrint(name="Hello",msg=name)

print()
print("--------------------Armstrong number------------------------")

def armStrong():
    num=int(input("Enter the number"))
    temp=tem=num
    count=0
    sum_=0
    while num>0:
        num=num//10
        count+=1
        #print (count)

    while temp>0:
        rem=temp%10
        temp//=10
        sum_=sum_+rem**count

    if sum_==tem:
        print("Armstrong number")
    else:
        print("Not a Armstrong number")

armStrong()

print()
print("--------------------Sum of Number------------------------")

def mySum(f,s,t):
    print("Sum of Number is:",f+s+t)
mySum(1,2,3)

print()
print("--------------------Power Calculation------------------------")

def myPow(num,power):
    sum_=1
    for cnt in range(1,power+1):
        if(cnt==4):
            continue
        else:
            pass
        sum_*=num
    print("Power Calculated is: ",sum_)
   
myPow(4,5)


print()
print("--------------------Sum Calculator------------------------")

def calc(n):
    if n==1:
        return 1
    return n+calc(n-1)
print ("Sum till the Number is :",calc(10))


print()
print("--------------------Factorial Calculator------------------------")

def calc(n):
    if n==1:
        return 1
    return n*calc(n-1)
num=int(input("Enter a number: "))
print ("Factorial of Number is :",calc(num))
    
   
    
    

    
    
