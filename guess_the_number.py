import random
count=0
while True:
    choice=input("Want to Guess the Number yes(y) or no(n)")
    if choice !='y' and count==0:
        print("Not Interested")
        break;
    elif choice!='y' and count>0:
        print("Thanks for playing")
        break;
    else:

        num=int(input("Enter the number between 1 to 9"))
        a=random.randrange(1,9)
        count +=1
        if a==num:
            print("You Guessed Right")
        else:
            print("Bad Luck")
    print("The number is............",end="")
    print(a)
print("------------------Game Over--------------------")

    
    

 
