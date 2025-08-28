#How many days, weeks and months left if you live for 90 years
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

age = input("Enter your current age: ")
years = 90 - int(age)
weeks = int(years) * 52
months = int(years) *12



print(f"you have {years} years, {weeks} weeks and {months} months, left")
