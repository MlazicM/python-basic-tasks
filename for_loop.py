# This program prints even numbers from 2 to 8 and counts how many numbers were printed.
count = 0  # Initialize counter
for number in range(2, 9, 2):  # Loop through even numbers from 2 to 8
    print(number)
    count += 1  # Increment counter
# Print the total count of even numbers printed, basic print with f-string.
print(f"Total even numbers printed: {count}")
