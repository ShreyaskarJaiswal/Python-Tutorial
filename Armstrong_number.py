num=int(input("Enter the number"))
temp=tem=num
count=0
sum=0
while num>0:
    num=num//10
    count+=1
#print (count)

while temp>0:
    rem=temp%10
    temp//=10
    sum=sum+rem**count

if sum==tem:
    print("Armstrong number")
else:
    print("Not a Armstrong number")
    
