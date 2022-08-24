l1,l2=[],[]
print()
n=int(input("Enter the number of elements in a Set 1"))
for i in range(n):
    a=int(input())
    l1.append(a)
set1=set(l1)
n=int(input("Enter the number of elements in a Set2"))
for i in range(n):
    b=int(input())
    l2.append(b)
set2=set(l2)

print("Set 1:",set1)
print("Set 2",set2)

# set union
print("Union of Set 1 and Set 2 is",set1 | set2)

# set intersection
print("Intersection of Set 1 and Set 2 is",set1 & set2)

# set difference
print("Difference of Set 1 and Set 2 is",set1 - set2)

# set symmetric difference
print("Symmetric difference of Set 1 and Set 2 is",set1 ^ set2)