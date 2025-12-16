# This program checks if a number is positive even, positive odd, zero, or negative.
n = int(input('Enter number: '))
if int(n) > 0:  # Checking if the number is positive
    if (n) % 2 == 0:
        print('Positive even number')
    else:
        print('Positive odd number')
elif (n) == 0:  # Checking if the number is zero
    print('You entered zero, there is no need to check for even or odd.')
elif (n) < 0:  # Checking if the number is negative
    n = (n) * -1
    # Converting negative to positive
    print(f'You entered a negative number {n}, its positive value is {n}.')
