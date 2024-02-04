import time
user_name = input("Enter Your Name: ")
timestamp = time.strftime("%H:%M:S")
hour = int(time.strftime("%M"))
print(timestamp)
print(user_name)
if hour < 10:
    print("Good moring!!", user_name)
else:
    print("Good Afternoon!!", user_name)

