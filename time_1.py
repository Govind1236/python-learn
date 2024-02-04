import time
name = input("Enter Your Name: ")
times = time.strftime("%I:%H:%M")
hour = int(time.strftime("%I"))
if hour < 12:
    print("Good morning!! " +  name.upper(), times)
else:
    print("Good afternoon!! " +  name.lower(), times)

