############# finds out the average height of the entered height using for loop ##############
student_heights = input("Enter the list heights \n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

################### to find out sum of heights using for loop ##################
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
###################### find the number of entered heights using for loop ############
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)


average_height = total_height / number_of_students
rounded_height = round(average_height, 2)
print(f"The average height of students is : {rounded_height}")
