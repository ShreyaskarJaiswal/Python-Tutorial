class Employee:

    def __init__(__self__,name,designation,salary):
        #print("Intializing values and creating object")
        print()
        
        __self__.name=name
        __self__.designation=designation
        __self__.salary=salary

    def getName(__self__):

        return __self__.name
        
    def getDesignation(__self__):

        return __self__.designation
        
    def getSalary(__self__):

         return __self__.salary
        
emp_data=[]
print("----------Welcome to my files---------")
print()

print("1.Enter Employee's Data\n2.Print Employee's Data\n3.Exit the menu")
ans =input("Want to enter the Employee's data (Y or N)\n")

while True:
    if ans!='y'and ans!='Y':
        print("No Data Present")
        break
        
    else:
        ser=0
        choice=input("Enter choice from the menu:")
        if choice=='1':

            u_name = input("Enter Employee's Name")
            u_deg =  input("Enter Employee's Designation")
            u_sal =  int(input("Enter Employee's Salary"))
            emp = Employee(u_name,u_deg,u_sal)
            emp_data.append(emp)

        elif choice=='p':
            for data in emp_data:
                ser+=1
                print(f"{ser}.Employee name: {data.getName()}, Designation: {data.getDesignation()},",end="")
                print(f" Salary: {data.getSalary()}")
                print()
        else:
            print()
            print("-------Thanks for the Details--------")
            break




