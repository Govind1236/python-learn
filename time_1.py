import time
name = input("Enter Your Name: ")
timestamp = time.strftime("%H:%M")
times = int(time.strftime('%H'))
print(name , timestamp)
if(times < 12 ):
    greet = name + "Good morning!!" + str(times)
    print(greet)
else:
    greet = name + "Good Afternoon!!" + str(times)
    print(greet)
