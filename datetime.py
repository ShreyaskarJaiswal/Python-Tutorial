import datetime as dt
import time

d_t= dt.datetime.now().time().hour
name=input("Enter your name\n")
if d_t<12 and d_t>6:
    print("Hello ",name)
    print ("Good morning")
    print("Today's date&time is\n",dt.datetime.now())
elif d_t>12 and d_t<16:
    print("Hello ",name)
    print("Good afternoon")
    print("Today's date&time is\n",dt.datetime.now())
elif d_t>16 and d_t<20:
    print("Hello",name)
    print("Good evening")
    print("Today's date&time is\n",dt.datetime.now().hour)
elif d_t>20 and d_t<6:
    print("Hello",name)
    print("Good night")
    print("Today's date&time is\n",dt.datetime.now().hour)




print("-----------------------------------")
print(time.localtime())
print(time.localtime().tm_year)
