
temperature_tmp = float(input("Enter a temperature in Fahrenheit: "))
if temperature_tmp < 32:
    print ("Below Freezing")
elif temperature_tmp > 32 or  temperature_tmp <= 212:
    print ("Freezing to boiling")
else:
    print ("Boiling and Above")
print("Input error")