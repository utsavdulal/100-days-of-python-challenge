#program to determine who will pay the bill takes your names and print random name from your input
import random
name_string = input("Enter everyone's names, sepatated by comma. ")
name = name_string.split(", ")

total_names = len(name)

random_choice = random.randint(0, total_names-1)
person_who_will_pay = name[random_choice]
print(f"{person_who_will_pay} will pay the bill today")