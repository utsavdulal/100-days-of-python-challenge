#############################Program to write a love calculator app########################
print("Welcome to love calculator app : \n")
your_name = input("Enter your Name : \n")
crush_name = input("Enter your crush's Name : \n")

low_name = your_name.lower()
low_crush = crush_name.lower()

both_name = low_name + low_crush

true = (
    both_name.count("t")
    + both_name.count("r")
    + both_name.count("u")
    + both_name.count("e")
)
love = (
    both_name.count("l")
    + both_name.count("o")
    + both_name.count("v")
    + both_name.count("e")
)

true_love = str(true) + str(love)
true_love = int(true_love)

if true_love < 10 or true_love > 90:
    print(f"Your love score is {true_love}, you go together like coke and mentos")

elif true_love >= 40 and true_love <= 50:
    print(f"Your love score is {true_love}, you are alright together")

else:
    print(f"Your love score is {true_love}")
