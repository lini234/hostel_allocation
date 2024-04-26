import json

# Function to normalize CGPA values to a scale of 0 to 1
def normalize_cgpa(cgpa):
    max_cgpa = 4.0  # Assuming CGPA scale is 0 to 4.0
    return cgpa / max_cgpa

# Function to calculate similarity score for course of study
def calculate_course_similarity(course1, course2):
    return 1.0 if course1 == course2 else 0.0

# Function to calculate similarity score for CGPA
def calculate_cgpa_similarity(cgpa1, cgpa2):
    normalized_cgpa1 = normalize_cgpa(cgpa1)
    normalized_cgpa2 = normalize_cgpa(cgpa2)
    difference = abs(normalized_cgpa1 - normalized_cgpa2)
    return 1.0 - difference

# Function to calculate similarity score for temperament
def calculate_temperament_similarity(temperament1, temperament2):
    return 1.0 if temperament1 == temperament2 else 0.0

# Function to calculate similarity score for cultural background
def calculate_cultural_similarity(cultural1, cultural2):
    return 1.0 if cultural1 == cultural2 else 0.0

# Function to calculate diversity score for a set of cultural backgrounds
def calculate_diversity_score(cultural_data):
    unique_cultures = set(cultural_data)
    num_cultures = len(unique_cultures)
    total_students = len(cultural_data)
    diversity_score = num_cultures / total_students
    return diversity_score

# Function to calculate overall compatibility score between two students
def calculate_compatibility_score(student1, student2, weights):
    course_similarity = calculate_course_similarity(student1['course'], student2['course'])
    cgpa_similarity = calculate_cgpa_similarity(student1['cgpa'], student2['cgpa'])
    temperament_similarity = calculate_temperament_similarity(student1['temperament'], student2['temperament'])
    cultural_similarity = calculate_cultural_similarity(student1['cultural'], student2['cultural'])
    cultural_data = [student1['cultural'], student2['cultural']]
    diversity_score = calculate_diversity_score(cultural_data)

    compatibility_score = (
        weights['course'] * course_similarity +
        weights['cgpa'] * cgpa_similarity +
        weights['temperament'] * temperament_similarity +
        weights['cultural'] * cultural_similarity +
        weights['diversity'] * diversity_score
    )
    return compatibility_score

# Load student data from JSON file
with open('students.json', 'r') as file:
    students_data = json.load(file)

# Define weights for compatibility algorithm
weights = {'course': 0.3, 'cgpa': 0.3, 'temperament': 0.2, 'cultural': 0.1, 'diversity': 0.1}

# Calculate compatibility scores and store them in a list
compatibility_scores = []
for i in range(len(students_data)):
    for j in range(i + 1, len(students_data)):
        student1 = students_data[i]
        student2 = students_data[j]
        compatibility_score = calculate_compatibility_score(student1, student2, weights)
        compatibility_scores.append((student1['student_id'], student2['student_id'], compatibility_score))

# Output or further process compatibility scores
print(compatibility_scores)
