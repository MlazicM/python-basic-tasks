# This program is a number guessing game where the user has to guess a randomly generated number between 1 and 100.
# Its simple yet fun to play!
import random
num_to_ges = random.randint(1, 100)
attempts = 0  # To count the number of attempts made by the user
while True:
    # Taking user input for the guess
    guess = int(input("Guess random number from 1 to 100: "))
    attempts += 1  # Incrementing the attempt count
    if guess > num_to_ges:
        print("You should go for a lower number")
    elif guess < num_to_ges:  # Checking if the guess is lower than the generated number
        print("You should go for a higher number")
    else:
        # User guessed the correct number
        print(f"Bravo! You guessed the right number in {attempts} attempts.")
        break  # Exiting the loop when the correct number is guessed
# This is where it ends, it was fun coding this simple game!
