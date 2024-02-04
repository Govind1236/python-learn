import time
name = input("Enter Your Name: ")
times = time.strftime("%H:%M")
hour = int(time.strftime("%M"))
if hour < 12:
    print("Good morning!! " +  name.upper)
else:
    print("Good afternoon!! " +  name)

