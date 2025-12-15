# Program to calculate the sum of integers from 0 to n-1
# Using built-in sum function
n = int(input("Enter a number n:"))
print(sum(range(0, n)))
# This program calculates and prints the sum of integers from 0 to n-1.
# It uses the built-in sum function along with range to achieve this.
# The range(0, n) generates numbers from 0 to n-1, and sum computes their total.
# This method is efficient and concise for calculating the sum of a sequence of integers.
# Lets see what we can do with a loop :DD
suma = 0
for i in range(0, n):
    suma += i
print(suma)
# This is another method to calculate the sum of integers from 0 to n-1 using a loop.
# It initializes a variable 'suma' to 0 and iterates through each integer in the range from 0 to n-1, adding each integer to 'sum'.
# Finally, it prints the accumulated sum.
