def binary_search(list, beg, end, search):
    if end >= beg:
        mid = (end + beg) // 2
        if list[mid] == search:
            return mid
        elif list[mid] > search:
            return binary_search(list, beg, mid - 1, search)
        else:
            return binary_search(list, mid + 1, end, search)
    else:
        return -1
list = [ 2, 3, 4, 10, 40 ]
search= 10
result = binary_search(list, 0, len(list)-1, search)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")