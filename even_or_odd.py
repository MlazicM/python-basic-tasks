n = int(input('Enter number: '))
if int(n) > 0:
    if (n) % 2 == 0:
        print('Positive even number')
    else:
        print('Positive odd number')
elif (n) == 0:
    print('You entered zero, there is no need to check for even or odd.')
elif (n) < 0:
    n = (n) * -1
    print(f'You entered a negative number {n}, his positive value is {n}.')
