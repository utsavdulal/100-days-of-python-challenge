##############program to print the heighest number among entered number by user ###################
students_score = input("Enter the list of students Scores \n ").split()
for n in range(0, len(students_score)):
    students_score[n] = int(students_score[n])
print(students_score)

#######################################################################################

highest_score = 0
for score in students_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score is : {highest_score}")
