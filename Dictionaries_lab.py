"""
Student Database - Dictionaries Laboratory
Simple student database using dictionaries
"""

# Task 3.1: Student Database
print("="*50)
print("TASK 3.1: STUDENT DATABASE")
print("="*50)

# Create empty dictionary for students
students = {}

# Function to add student
def add_student(student_id, name, grade, major):
    students[student_id] = {
        'name': name,
        'grade': grade,
        'major': major
    }
    print(f"Added student: {name} (ID: {student_id})")

# Function to get student by ID
def get_student(student_id):
    if student_id in students:
        return students[student_id]
    else:
        print(f"Student {student_id} not found!")
        return None

# Function to update grade
def update_grade(student_id, new_grade):
    if student_id in students:
        old_grade = students[student_id]['grade']
        students[student_id]['grade'] = new_grade
        print(f"Updated {students[student_id]['name']}'s grade from {old_grade} to {new_grade}")
    else:
        print(f"Student {student_id} not found!")

# Function to display all students
def display_all_students():
    print("\nAll Students:")
    print("-" * 40)
    for student_id, info in students.items():
        print(f"ID: {student_id}")
        print(f"  Name: {info['name']}")
        print(f"  Grade: {info['grade']}")
        print(f"  Major: {info['major']}")
        print()

# Add sample students
add_student("CS001", "tanggol nazareno", "A", "Computer Science")
add_student("CS002", "cardo dalisay", "B", "Computer Science")
add_student("EE001", "milky brown", "A", "Electrical Engineering")

# Display all students
display_all_students()

# Get a specific student
print("Getting student CS002:")
student = get_student("CS002")
if student:
    print(f"Found: {student}")

# Update a grade
print("\nUpdating grade:")
update_grade("CS002", "A")

# Display all students again
display_all_students()

# Task 3.2: Word Frequency Counter
print("="*50)
print("TASK 3.2: WORD FREQUENCY COUNTER")
print("="*50)

# Sample text
text = "Python is fun. Python is easy. Programming is fun."
print(f"Sample text: \"{text}\"")

# Clean text and split into words
clean_text = text.lower().replace(".", "")
words = clean_text.split()

# Count word frequencies using dictionary
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Display word frequencies
print("\nWord frequencies:")
for word, count in word_freq.items():
    print(f"  '{word}': {count} times")

# Find most common word
most_common = ""
max_count = 0
for word, count in word_freq.items():
    if count > max_count:
        max_count = count
        most_common = word

print(f"\nMost common word: '{most_common}' (appears {max_count} times)")