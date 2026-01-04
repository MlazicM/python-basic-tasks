grades = []
num_students = int(input("Enter number of students: "))

for i in range(num_students):
    while True:
        try:
            g = int(input(f"Enter grade for student {i+1} (1-5): "))
        except ValueError:
            print("Please enter an integer between 1 and 5.")
            continue
        if 1 <= g <= 5:
            grades.append(g)
            break
        print("Invalid grade. Please enter a grade between 1 and 5.")

average = sum(grades) / len(grades)
min_grade = min(grades)
max_grade = max(grades)
a = grades.count(5)
print("Average grade:", average)
print("Minimum grade:", min_grade)
print("Maximum grade:", max_grade)
print("Number of students with grade 5:", a)
