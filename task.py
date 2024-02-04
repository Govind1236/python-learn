# Write a Python program that takes a student's
# score as an input and checks and prints their corresponding grade. Use the following grading scale:

#     A: 90-100
#     B: 80-89
#     C: 70-79
#     D: 60-69
#     F: 0-59
score = int(input("Enter Your Marks You Obtained: "))
if score >= 90:
    print("Your Grade of ", score, "is A")
elif score >= 80:
    print("Your Grade of ", score, "is B")
elif score >= 70:\
    print("Your Grade of ", score, "is C")
elif score >= 60:
    print("Your Grade of ", score, "is D")
else:
    print("Your Grade of ", score, "is F")
    
    
          