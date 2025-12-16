# This program checks if the user is eligible based on their age.
age = input("How old are you? ")
# Using a conditional expression to determine eligibility
message = "You are eligible " if int(age) >= 18 else "You are not eligible"
print(message)
