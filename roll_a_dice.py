import random
print("--------------------------Roll the Dice---------------------------------")
while True:
    
    n=input("Want to roll a dice yes(y) or no(n)")
    a = random.randrange(1,6)
    if(n=='y'):
        print("Rolling.........",end="")
        print(a)
    else:
        print("Rolling Stops")
        break
        
        

