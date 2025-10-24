"""
Student Grade Manager - Lists Laboratory
Simple program to manage student grades using lists
"""

# Task 1.1: Student Grade Manager
print("TASK 1.1: STUDENT GRADE MANAGER")
print()  # Blank line to match expected output

# Create empty lists
student_names = []
student_grades = []

# Function to add student
def add_student(name, grade):
    student_names.append(name)
    student_grades.append(grade)
    print(f"Added {name} with grade {grade}")

# Function to calculate average
def calculate_average():
    if len(student_grades) == 0:
        return 0
    return sum(student_grades) / len(student_grades)

# Function to find highest grade
def find_highest_grade():
    if len(student_grades) == 0:
        return 0
    return max(student_grades)

# Function to display all students
def display_students():
    print("\nStudent Grades:")
    for i in range(len(student_names)):
        print(f"{student_names[i]}: {student_grades[i]}")

# Add sample students - EXACT OUTPUT AS REQUIRED
add_student("Alice", 85)
add_student("Bob", 92)
add_student("Charlie", 78)

# Display results - EXACT FORMAT AS REQUIRED
display_students()

# Calculate and display statistics - EXACT FORMAT
avg = calculate_average()
highest = find_highest_grade()
print(f"\nAverage Grade: {avg:.1f}")  # Shows 85.0
print(f"Highest Grade: {highest}")     # Shows 92

print("\n" + "="*50)

# Task 1.2: List Operations Practice
print("TASK 1.2: LIST OPERATIONS PRACTICE")
print("="*50)

# Create list of numbers
numbers = [5, 2, 8, 1, 9, 3]
print(f"Original list: {numbers}")

# Sort the list
numbers.sort()
print(f"Sorted list: {numbers}")

# Calculate sum
total = sum(numbers)
print(f"Sum: {total}")

# Calculate average
average = total / len(numbers)
print(f"Average: {average:.2f}")

# Find max and min
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

# Find length
print(f"Length: {len(numbers)}")