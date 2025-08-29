#treasure island game
print('''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure island your mission is to find the Treasure! \n")
# print("You're middle of nowhere where do you wanna go 'left' or 'right' ?\n")
choice1 = input('You are middle of nowhere where do you wanna go "left" or "right" ?\n').lower()

if choice1 == "left":
    choice2 = input('YOu\'ve come acorss the lake. Type "wait" to wait for a boat and type "swim" to swim across. \n').lower()
    if choice2 == "wait":
       choice3 = input('you have reached to an island unharmed. There are three doors "Red", "Yellow" and "Blue" which one do you wanna choose? \n').lower()
       if choice3 == "red":
           print("You got burned by fire ! Game Over")
       elif choice3 == "blue":
           print("Blue slime got stuck in your butt ! Game Over")
       elif choice3 == "yellow":
           print("Your win!")
       else:
           print("Bitch choose the right door ! Game Over")
    else:
        print("Daddy Crocodile fucked your ass inside a lake! you died")
else:
    print("Shit a huge bull fucked you yeally good! you died")