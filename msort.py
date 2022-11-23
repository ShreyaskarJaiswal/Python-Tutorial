def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

num = int(input("Enter the number of element in the list: "))
data = []
for i in range(num):
    a = int(input())
    data.append(a)
print("Enter list: ", data)
size = len(data)
mergeSort(data)
print("Sorted List in Ascending Order : ")
print(data)
