from collections import Counter
# This program analyzes a series of numbers input by the user.


def main():  # Main function to analyze numbers
    numbers = []
    while True:
        s = input("Enter a number (0 to finish): ").strip()
        if s == "":
            print("Empty input; please enter a number or 0 to finish.")
            continue
        try:
            num = float(s)
        except ValueError:
            print("Invalid number; try again.")
            continue
        if num == 0:
            break
        numbers.append(num)

    if not numbers:  # Handle case with no numbers entered
        print("No numbers entered.")
        return
# Calculate statistics
    count = len(numbers)
    average = round(sum(numbers) / count, 2)
    minimum = min(numbers)
    maximum = max(numbers)
    count_positive = sum(1 for n in numbers if n > 0)
    count_negative = sum(1 for n in numbers if n < 0)
    freq = Counter(numbers)
    most_common_val, freq_count = freq.most_common(1)[0]
# Print results
    print(f"Count: {count}")
    print(f"Average: {average}")
    print(f"Positive numbers: {count_positive}")
    print(f"Negative numbers: {count_negative}")
    print(
        f"Most frequent number: {most_common_val} (appeared {freq_count} times)")
    print(f"Minimum number: {minimum}")
    print(f"Maximum number: {maximum}")


# Entry point
if __name__ == "__main__":
    main()
# End of number_analyzer.py
