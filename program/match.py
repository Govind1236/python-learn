num = int(input("Enter Number: "))
num1 = int(input("Enter Second Number:  "))
operation = input("Enter Operation to perform: ")
match operation:
    case "+" :
           operation =  num + num1
           print (operation)
    case '-' :
        operation = num - num1
        print (operation)
    case '/':
         operation = num / num1
         print(operation)
    case '*':
         operation = num * num1
         print(operation)
    case _ :
          print("invalid")

         

