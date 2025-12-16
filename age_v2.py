# This program checks if the user is eligible based on their age.
age = input("How old are you? ")
# Age should be between 18 and 75 to be eligible.
if int(age) >= 18 and int(age) <= 75:  # This is chekking the age range.
    print("You are eligible")
else:
    print("You are not eligible, sorry.")
