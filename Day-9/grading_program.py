student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# creating an empty dictionary called student_grades
student_grades = {}

# code to add the grades to student_grades
for student, scores in student_scores.items():
    if scores >= 91:
        student_grades[student] = "Outstanding"
    elif scores >= 81:
        student_grades[student] = "Exceeds expectation"
    elif scores >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
# printing the converted grades
print(student_grades)
