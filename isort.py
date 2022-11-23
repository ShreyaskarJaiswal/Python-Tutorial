def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
    j = step-1
    while j >= 0 and key < array[j]:
        array[j+1] = array[j]
        j = j-1
    array[j+1] = key

num = int(input("Enter the number of element in the list : "))
data = []
for i in range(num):
    a = int(input())
    data.append(a)
print("Enter list: ", data)
size = len(data)
insertionSort(data)
print("Sorted list in Ascending order : ")
print(data)