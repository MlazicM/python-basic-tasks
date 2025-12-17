def multiplicaton(numbers):
    multiplicator = 1
    for number in numbers:
        multiplicator *= number
    return multiplicator


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Result is : {multiplicaton(numbers)}")
