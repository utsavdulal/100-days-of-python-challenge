#BMI upgraded version BMI 2.0 
height = float(input("Enter your height in M: \n"))
weight = float(input("Enter your weight in kg : \n"))

bmi = weight / (height **2)
print(f"Your BMI is : {round(bmi, 2)}")
#applying different conditions

if bmi < 18.5 :
    print("You are underweight")
elif bmi < 25:
    print("you're normal weight")
elif bmi < 30:
    print("you're overweight")
elif bmi < 35 :
    print("you're obese")
else:
    print("you're clinically obese")


