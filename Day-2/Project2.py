#Tip calculator + bill splitter app
print("welcome to the tip calculator \n")

#asking user for input
bill = input("what was the total bill? \n")
tip_percentage = input("What percent of amount do you wanna tip? \n")
people = input("Enter the number of people you wanna split the bill with \n")

#adding tip to the total bill
tip_amount = float(tip_percentage) / 100  * float(bill)
total_bill = float(tip_amount) + float(bill)

#spliting the bill to entered people
split = float(total_bill) / float(people)

#printing the result
print(f"you have to pay $: {round(split, 2)}")