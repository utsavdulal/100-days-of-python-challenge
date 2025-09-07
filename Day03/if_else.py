#########program to differenciate either you can ride a rollarcoster of not according to your height###########

height = int(input("Enter your height in CM: \n "))

################making the condition either you can ride or not (if else statement)###################

# if height >= 120 :
#     print("You can ride!")

# else:
#     print("you can't ride!")


############Nested if else statement to check your ticket price and if you can ride or not###################
if height >= 120 :
    print("You can ride!")
    age = int(input("Enter your age: \n"))
    bill = 0

    if age > 18:
        bill = 12
        print("Adult ticket is : $12")
    elif age < 12:
        bill = 5
        print("Child ticket is : $5")
    else:
        bill = 7
        print("Youth ticket is : $7")

    want_photos = input("Do you want ride photos ? Y OR N.")
    if want_photos == "Y":
        print(f"Your total bill is : {bill + 3}")
    else:
        print(f"Your total bill is : {bill}")
else:
    print("you can't ride you're too short !")
    