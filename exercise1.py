import time
name = input("Enter Your Name: ")
timestamp = time.strftime("%I:%M")
print(name)
print(timestamp)
if(timestamp == 0):
    print("Good morning")
elif(timestamp < 0 and timestamp > 10):
    print("Welcome")