std_grade = float((input("Enter Your Marks: ")))
match std_grade:
    case grade if (90 < grade <= 100):
        print("Your Grade is A")
    case grade if (grade > 80):
        print("Your Grade is B")
    case grade if (grade > 70):
        print("Your Grade is c")
    case _ :
        print("Your Grade is F")