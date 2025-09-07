height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

heighsq = float(height)**2
weightfl = float(weight)

bmi = int(weightfl) / int(heighsq)
print(int(bmi))




###################### another code with diff pattern ###################

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")



bmi = int(weight) / float(height)**2

print(int(bmi))