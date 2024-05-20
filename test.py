import json
import matplotlib.pyplot as plt

# Function to normalize CGPA values to a scale of 0 to 1
def normalize_cgpa(cgpa):
    max_cgpa = 5.0  # Assuming CGPA scale is 0 to 5.0
    return cgpa / max_cgpa

# Function to calculate similarity score for course of study
def calculate_course_similarity(course1, course2, faculty1, faculty2):
    if course1 == course2 and faculty1 == faculty2:
        return 100
    elif faculty1 == faculty2:
        return 70
    else:
        return 0

# Function to calculate similarity score for CGPA
def calculate_cgpa_similarity(cgpa1, cgpa2):
    normalized_cgpa1 = normalize_cgpa(cgpa1)
    normalized_cgpa2 = normalize_cgpa(cgpa2)
    difference = abs(normalized_cgpa1 - normalized_cgpa2)
    return max(0, 100 - difference * 100)

# Function to calculate similarity score for state
def calculate_state_similarity(state1, state2):
    return 0 if state1 == state2 else 30

# Function to calculate similarity score for geopolitical zone
def calculate_zone_similarity(zone1, zone2):
    return 50 if zone1 == zone2 else 70

# Function to calculate overall compatibility score between two students
def calculate_compatibility_score(student1, student2, weights):
    course_similarity = calculate_course_similarity(student1['course'], student2['course'], student1['faculty'], student2['faculty'])
    cgpa_similarity = calculate_cgpa_similarity(student1['cgpa'], student2['cgpa'])
    state_similarity = calculate_state_similarity(student1['state'], student2['state'])
    zone_similarity = calculate_zone_similarity(student1['zone'], student2['zone'])

    compatibility_score = (
        weights['course'] * course_similarity +
        weights['cgpa'] * cgpa_similarity +
        weights['state'] * state_similarity +
        weights['zone'] * zone_similarity
    )
    return compatibility_score

# Load student data from JSON file
with open('students.json', 'r') as file:
    students_data = json.load(file)

# Define weights for compatibility algorithm
weights = {'course': 0.3, 'cgpa': 0.3, 'state': 0.2, 'zone': 0.2}

# Calculate compatibility scores for all pairs of students
compatibility_scores = []
for i, student1 in enumerate(students_data):
    for j, student2 in enumerate(students_data):
        if i != j:
            score = calculate_compatibility_score(student1, student2, weights)
            compatibility_scores.append({'students': (student1['student_id'], student2['student_id']), 'score': score})

# Sort compatibility scores
sorted_scores = sorted(compatibility_scores, key=lambda x: x['score'], reverse=True)

# Print the top 6 most compatible students
print("Top 6 Most Compatible Student Pairs:")
for i in range(6):
    pair = sorted_scores[i]['students']
    score = sorted_scores[i]['score']
    print(f"Compatibility between Student {pair[0]} and Student {pair[1]}: {score:.2f}%")

