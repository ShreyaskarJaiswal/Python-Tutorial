list_=[1,3,8,7,5,6]

list_a=['BabuRao','Shyam','Raju']
list_b=[25,'Raju',50]

print(list_.index(8))
print(list_.pop())
var=list_.copy()
print(var)


print(8 in list_)
print(10 in list_)
print("-------------------------")
print(8 not in list_)
print(8 not in list_)


print(list_)
print(list_a)
print(list_b)

print(list_a[2])
print(list_[-4])

for count in range(len(list_)):
    print(list_[count],end=" ")

print()

for count in list_:
    print(count,end=" ")

print()

list_[2]=20
list_[2:2]=[99,45,56]
list_.insert(2,[5,6,21])
list_.append(52)
print(list_[2:5])
print(list_[:])
print(list_[2][1])
#var=list_[2]
#print(var[1])
#list_.clear()
del list_[2]
list_.remove(52)

print(list_)






