import time
user_name = input("Enter Your Name: ")
# timestamp = time.strftime("%H:%M:S")
hour = int(time.strftime("%M"))
if hour < 12:
    print("Good moring!!", user_name)
else:
    print("Good Afternoon!!", user_name)

