"""
Student Records File System - File Handling Laboratory
Simple file operations for student records
"""
import pickle

# Task 4.1: Student Records File System
print("="*50)
print("TASK 4.1: STUDENT RECORDS FILE SYSTEM")
print("="*50)

# Create sample student records
student_records = [
    {'id': 'CS001', 'name': 'cardo', 'grade': 'A', 'major': 'Computer Science'},
    {'id': 'CS002', 'name': 'tanggol', 'grade': 'B', 'major': 'Computer Science'},
    {'id': 'EE001', 'name': 'domeng', 'grade': 'A', 'major': 'Electrical Engineering'}
]

print("Original student records:")
for record in student_records:
    print(f"  {record}")

# Function to save records using pickle
def save_records(records, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(records, file)
        print(f"\n Saved {len(records)} records to {filename}")
        return True
    except Exception as e:
        print(f"\n Error saving: {e}")
        return False

# Function to load records using pickle
def load_records(filename):
    try:
        with open(filename, 'rb') as file:
            records = pickle.load(file)
        print(f"\n Loaded {len(records)} records from {filename}")
        return records
    except FileNotFoundError:
        print(f"\n File {filename} not found")
        return None
    except Exception as e:
        print(f"\n Error loading: {e}")
        return None

# Function to export to text file
def export_to_text(records, filename):
    try:
        with open(filename, 'w') as file:
            file.write("STUDENT RECORDS\n")
            file.write("=" * 40 + "\n\n")
            
            for record in records:
                file.write(f"ID: {record['id']}\n")
                file.write(f"Name: {record['name']}\n")
                file.write(f"Grade: {record['grade']}\n")
                file.write(f"Major: {record['major']}\n")
                file.write("-" * 20 + "\n")
            
            file.write(f"\nTotal Records: {len(records)}\n")
        
        print(f"Exported records to {filename}")
        return True
    except Exception as e:
        print(f"Error exporting: {e}")
        return False

# Save records to pickle file
save_records(student_records, "students.pkl")

# Load records from pickle file
loaded_records = load_records("students.pkl")
if loaded_records:
    print("\nLoaded records:")
    for record in loaded_records:
        print(f"  {record}")

# Export to text file
export_to_text(student_records, "students.txt")

# Task 4.2: File Operations Practice
print("\n" + "="*50)
print("TASK 4.2: FILE OPERATIONS PRACTICE")
print("="*50)

# Write mode ('w')
print("\n1. Writing to a file:")
try:
    with open("test.txt", 'w') as file:
        file.write("This is line 1\n")
        file.write("This is line 2\n")
    print("    File created and written")
except Exception as e:
    print(f"    Error: {e}")

# Read mode ('r')
print("\n2. Reading from a file:")
try:
    with open("test.txt", 'r') as file:
        content = file.read()
    print("   File content:")
    print("   " + content)
except FileNotFoundError:
    print("    File not found")
except Exception as e:
    print(f"    Error: {e}")

# Append mode ('a')
print("3. Appending to a file:")
try:
    with open("test.txt", 'a') as file:
        file.write("This line was appended\n")
    print("    Content appended")
except Exception as e:
    print(f"   Error: {e}")

# Read again to show append worked
print("\n4. Reading after append:")
try:
    with open("test.txt", 'r') as file:
        lines = file.readlines()
    print(f"   File now has {len(lines)} lines:")
    for i, line in enumerate(lines, 1):
        print(f"   Line {i}: {line.strip()}")
except Exception as e:
    print(f"  Error: {e}")

# Error handling example
print("\n5. Error handling:")
try:
    with open("nonexistent.txt", 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("   Handled FileNotFoundError correctly")

print(" File operations completed!")