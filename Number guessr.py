import random
num_to_ges = random.randint(1,100)
attempts=0
while True:
    guess=int(input("Guess random number from 1 to 100: "))
    attempts+=1
    if guess > num_to_ges:
        print("You should go for a lower number")
    elif guess< num_to_ges:
        print("You should go for a higher number")
    else:
        print(f"Bravo! You guessed the right number in {attempts} attempts.`")
        break



