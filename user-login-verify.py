user_name = input("Enter Your Name: ")
user_pass  = input("Enter Password: ")
login = user_name == 'user' and user_pass == 'user@123'
if (login):
    print("Success")
else:
    print("Login fail")
    