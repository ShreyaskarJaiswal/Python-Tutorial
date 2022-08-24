
print("------------Pattern 1------------")
for row in range(1,6):
    for col in range (1,row+1):
        print("*",end=" ")
    print()

print("------------Pattern 2------------")
for row in range(6):
    for col in range (6-row):
        print(" ",end=" ")
    for mid in range (row):
         print("*",end=" ")
    print()

print("------------Pattern 3------------")

a=int(input("Enter the num"))
for i in range(a+1):
    print(" "*(a-i)+ " *"*i)
for i in range(a-1,0,-1):
    print(" "*(a-i)+" *"*i)

print("------------Pattern 4------------")

a=int(input("Enter the num"))
for i in range(a+1):
    print(" "*(a-i)+ " *"*i)
for i in range(a-1,0,-1):
    print(" "*(a-i)+" *"*i)


    
    
   


       
                                                                                     
