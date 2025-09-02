import random
from hangman_words import word_list
from hangman_arts import stages
from hangman_arts import logo

# list of words for hangman
hangman_words = word_list

# Randomly choose the words form the above list
chosen_word = random.choice(hangman_words)
print(chosen_word)

# importing and printing hangman logo from hangman_arts
print(logo)

# create a display list with "_" for each letter in the word
display = []
word_length = len(chosen_word)

# Total guesses allowed
lives = 6

# to display the _ in place of words to be input by user
for _ in range(word_length):
    display += "_"
print(display)  # to show the starting blanks _

# game loop runs until playes wins or loses
end_of_game = False

while not end_of_game:
    # input from the user
    guess = input("Guess a letter \n").lower()

    # let player know if they have already entered the number
    if guess in display:
        print("YOu've already entered this letter ! enter next")

    # check every postion in the word
    for position in range(word_length):
        letter = chosen_word[position]
        # if the guessed letter matches then replace it in the place of blank(_)
        if letter == guess:
            display[position] = letter

    # checks if player is wrong
    if guess not in chosen_word:
        if guess not in chosen_word:
            print(f"{guess} is not in the list - you lose a life")
        lives -= 1  # if guesses letter is wrong loose 1 life
        if lives == 0:
            end_of_game = True
            print("You lose !")  # if player lose all the lives then print "You lose !"

    # joins all the elements in the list
    print(f"{' '.join(display)}")

    # checks if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("you win!")

    # prints the ascii art according to game
    print(stages[lives])
