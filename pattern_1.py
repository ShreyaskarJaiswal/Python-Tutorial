
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
for row in range(6):
    for col in range (6-row):
        print(" ",end=" ")
    for mid in range (row):
         print("*",end=" ")
    print()

    
        
                                                                                     
