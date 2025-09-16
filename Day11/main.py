import random
from clear_function import clear  # Function to clear the console screen
from art import logo  # ASCII logo for Blackjack game


# -------------------- CARD & SCORE FUNCTIONS --------------------


def deal_card():
    """Return a random card from the deck.

    The deck contains numbers 2–10 and face cards (all counted as 10).
    Ace (11) can also be used, which may later convert to 1 if needed.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the total score.

    Special Rules:
    - Blackjack (Ace + 10) is represented as 0 for easy comparison.
    - If total > 21 and there is an Ace (11), convert one Ace to 1.
    """
    # Check for a Blackjack (only 2 cards: Ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Convert Ace (11) to 1 if score goes over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    """Compare user and computer scores and return the game result as a string."""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "You lose, opponent has a Blackjack 🙀"
    elif user_score == 0:
        return "Blackjack! You win 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😉"
    elif user_score > computer_score:
        return "You win ☺️!"
    else:
        return "You lose 😭"


# -------------------- MAIN GAME FUNCTION --------------------


def play_game():
    """Run a single game of Blackjack."""

    print(logo)  # Display Blackjack ASCII art

    # Start with 2 cards each
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # End game if someone has Blackjack or user goes over 21
        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn (draw cards until score is at least 17, unless it's Blackjack)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final results
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# -------------------- GAME LOOP --------------------

# Keep asking the user if they want to play again
while (
    input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y"
):
    clear()  # Clear the console for a fresh game
    play_game()
