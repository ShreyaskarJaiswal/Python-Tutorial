String = input("Enter a String")

dict= {}

list = String.split(".")

for elements in list:
	if elements == '.':
		elements= " " 
	if elements in dict:
		dict[elements] += 1
	else:
		dict.update({elements: 1})

print(dict)

