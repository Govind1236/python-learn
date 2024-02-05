user_name = input("Enter Your Name: ")
user_pass  = input("Enter Password: ")
login = user_name + user_pass
match login:
    case _ if(user_name == 'user' and user_pass == 'user@123'):
        print("login Success ")
    case _ :
        print("Login Denide")


