num = int(input("Enter the number of elements in the list: "))
list = []
for i in range(num):
    a = int(input())
    list.append(a)
print("Entered List", list)
list.sort()
print("Sorted List", list)
search = int(input("Enter the element you want to search: "))
beg, end = 0, len(list)
while beg <= end:
    mid = (beg+end)//2
    if list[mid] < search:
        beg = mid + 1
    elif list[mid] > search:
        end = mid - 1
    else:
        break

if(search ==list[mid]):
    print(f"Search element found at position {mid+1}")
else:
    print("Element does not exist in the list")