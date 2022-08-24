list1=[]
list2=[]
list3=[]
print("-----------FCFS SCHEDULING ALGORITHM----------")
wt,awt,tt,att=0,0,0,0
n=int(input("Enter the number of Process "))
for i in range(n):
    print("Burst time of P",i+1,"in ms:")
    l1=int(input())
    list1.append(l1)

print("-----------WAITING TIME OF THE PROCESSES----------")
print("Waiting time of P 1 is : 0 ms")
for i in range (n-1):
    wt+=list1[i]
    list2.append(wt)
    print("Waiting time of P",i+2,"is :",wt,"ms")
    awt+=list2[i]
print("Average waiting time of the processes :",awt/n,"ms")
print()

print("-----------TURNAROUND TIME OF THE PROCESSES----------")
for i in range (n):
    tt+=list1[i]
    list3.append(tt)
    print("Turnaround time of P",i+1,"is :",tt,"ms")
    att+=list3[i]
print("Average Turnaround time of the processes :",att/n,"ms")
