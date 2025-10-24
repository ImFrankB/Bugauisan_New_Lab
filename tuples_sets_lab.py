"""
Coordinates and Word Counter - Tuples & Sets Laboratory
Simple demonstrations of tuples and sets
"""
import math

# Task 2.1: Coordinate System with Tuples
print("="*50)
print("TASK 2.1: COORDINATE SYSTEM WITH TUPLES")
print("="*50)

# Define points as tuples
point1 = (0, 0)
point2 = (3, 4)
point3 = (6, 8)

# Create tuple containing all points
all_points = (point1, point2, point3)

print("Points defined:")
print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
print(f"Point 3: {point3}")

# Function to calculate distance
def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Function to find midpoint
def find_midpoint(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    return (midpoint_x, midpoint_y)

# Calculate distances
print("\nDistances:")
print(f"Distance from {point1} to {point2}: {calculate_distance(point1, point2):.2f}")
print(f"Distance from {point2} to {point3}: {calculate_distance(point2, point3):.2f}")

# Find midpoints
print("\nMidpoints:")
print(f"Midpoint between {point1} and {point2}: {find_midpoint(point1, point2)}")
print(f"Midpoint between {point2} and {point3}: {find_midpoint(point2, point3)}")

# Demonstrate tuple immutability
print("\nDemonstrating tuple immutability:")
test_tuple = (1, 2, 3)
print(f"Original tuple: {test_tuple}")
try:
    test_tuple[0] = 5  # This will cause an error
except TypeError:
    print("Error: Cannot modify tuple - tuples are immutable!")

# Task 2.2: Unique Word Counter with Sets
print("\n" + "="*50)
print("TASK 2.2: UNIQUE WORD COUNTER WITH SETS")
print("="*50)

# Sample text
text = "Python is a programming language. Python is easy to learn. Python is powerful."
print(f"Sample text: \"{text}\"")

# Split into words and convert to lowercase
words = text.lower().replace(".", "").split()

# Create set of unique words
unique_words = set(words)

# Count total and unique words
total_words = len(words)
unique_count = len(unique_words)

print(f"\nTotal words: {total_words}")
print(f"Unique words: {unique_count}")
print(f"Unique words list: {sorted(unique_words)}")

# Find most common word
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Find the most common word
most_common_word = ""
max_count = 0
for word, count in word_count.items():
    if count > max_count:
        max_count = count
        most_common_word = word

print(f"\nMost common word: '{most_common_word}' (appears {max_count} times)")