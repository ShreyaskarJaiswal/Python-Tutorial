num=int(input("Enter the number of elements in the list: "))
list=[]
for i in range(num):
    a=int(input())
    list.append(a)
print("Entered List",list)
search=int(input("Enter the element you want to search: "))                                                        
for i in range(num):
    if search==list[i]:
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print(f"Search element found at position {i+1}")
else:
    print("Element does not exist in the list") 
