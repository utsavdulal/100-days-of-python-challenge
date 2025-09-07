#python program to create automatic pizza order program
print("Welcome to python Pizza Deliveries!")
size = input("what size pizza do you want? S, M or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

total_bill = 0

if size == "S":
    total_bill +=15
    if add_pepperoni == "Y":
        total_bill += 2

elif size == "M":
    total_bill += 20
    if add_pepperoni == "Y":
        total_bill +=3

elif size == "L":
    total_bill += 25
    if add_pepperoni == "Y":
        total_bill +=3

#if you want extra cheese
if extra_cheese == "Y":
    total_bill += 1

print(f"your final bill is : {total_bill}")




#################### SAME CODE OF DIFFERENT FORMAT ###############################


    
if size == "S":
    total_bill += 15
elif size =="M":
    total_bill += 20
elif size == "L":
    total_bill += 25


if add_pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3

if extra_cheese == "Y":
    total_bill += 1

print(f"Your final bill is : {total_bill}")
