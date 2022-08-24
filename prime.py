num= int(input("Enter the number"))
flag=1
if (num==2):
    flag=1
else:
    for i in range(2,num//2):
        if(num%i==0):
            flag=0
            break
        else:
            flag=0
if(flag==1):
    print("Prime number")
else:
    print("not a prime number")
