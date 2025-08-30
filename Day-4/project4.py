# Rock Paper Scissor game using python
import random

rock = "👊"
paper = "📄"
scissor = "✂️"

choice = [rock, paper, scissor]

# taking input from user
human = int(input("Enter 0 for 👊, 1 for 📄 and 2 for ✂️ \n"))

# idetifying either the entered number is valid or not if yes. computer prints the random number
if human < 0 or human > 2:
    print("Invalid Input please enter valid number. 0, 1 or 2")
else:
    computer = random.randint(0, 2)

####### printing your input and computer's input ################
print(f"Your choice : {choice[human]}")
print(f"Cpmputer's choice : {choice[computer]}")

######## now using conditional statement to identify who wins #########

if human == computer:
    print("It's a draw. Play again!")
elif (
    human == 0
    and computer == 2
    or human == 1
    and computer == 0
    or human == 2
    and computer == 1
):
    print("You Win !")
else:
    print("You Loose")
