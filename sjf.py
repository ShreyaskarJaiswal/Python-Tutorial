n = int(input("Enter the number of process:"))
pid = [0]*n
for i in range(n):
    pid[i] = i+1
bt = []
print("Enter the burst time of the process:")
for j in range(n):
    p = input("")
    bt.append(p)
for i in range(n):
    min = i
    for j in range(i+1, n):
        if bt[min] > bt[j]:
            min = j
    bt[i], bt[min] = bt[min], bt[i]
    pid[i], pid[min] = pid[min], pid[i]
wt = [0]*n
tat = [0]*n
ct = [0]*n
sum = 0
for i in range(n):
    ct[i] = sum+int(bt[i])
    sum = ct[i]
for i in range(n):
    tat[i] = ct[i]
for i in range(n):
    wt[i] = tat[i]-int(bt[i])
print(f"Process Id\tBurst Time\tTurn Around Time\tWaiting Time")
for i in range(n):
    print(f"{pid[i]}\t\t{bt[i]}\t\t{tat[i]}\t\t\t{wt[i]}")
awt, atat = 0, 0
for i in range(n):
    awt = awt+wt[i]
    atat = atat+tat[i]
awt = awt/n
atat = atat/n
print(f"Average Turn Around Time is {atat}")
print(f"Average Waiting Time is {awt}")
