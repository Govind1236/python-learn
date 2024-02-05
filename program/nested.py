name = input("Enter a name: ")
age = int(input("Enter a Number: "))
print(age,name)
if(age==0):
    print("Number is Zero")
elif(age!=18):
    if(age<18):
        print("not eligible For driving")
    elif(age>=18):
        print("Your eligible to drive")
    else:
        print("Become matured")

else:
    print("Become 18 first")