# This program reads in a student's percentage mark and prints out the corresponding grade
# Percentages entered as floats need to be rounded before the grading
# Under 40%: Fail
# Between 40% and 49%: Pass
# Between 50% and 59%: Merit 2
# Between 60% and 69%: Merit 1
# Over 70%: Distrinction
# Author: Stefanie Steffens

percentage = float(input("Enter the percentage: "))

# Round the float percentate
roundPercentage = round(percentage)

# The first step checks that the entered number is a valid percentage, i.e. between 0 and 100
if roundPercentage < 0 or roundPercentage > 100:
    print("Please enter a number between 0 and 100")
elif roundPercentage >= 70:
    print("Distinction")
elif roundPercentage >= 60:
    print("Merit 1")
elif roundPercentage >= 50:
    print("Merit 2")
elif roundPercentage >= 40:
    print("Pass")
else:
    print("Fail")