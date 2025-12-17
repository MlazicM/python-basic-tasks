# This program greets the user and asks about their well-being.
def say_hi():  # Function to greet the user
    print("Hi there!")
    print("How are you?")


say_hi()
answer = input().strip().lower()  # Get user input and normalize it

negative = ("not good", "not well", "so so", "bad")
positive = ("good", "fine", "well")
# Respond based on the user's input

# Check for negative responses
if any(neg in answer for neg in negative):
    print("Things will get better soon, don't worry!")
elif any(pos in answer for pos in positive):
    print("Great to hear that!")  # Check for positive responses


# Basic program structure with function definition and user interaction, handling different user inputs.
# Funny and simple way to learn function calls and conditionals in Python.
