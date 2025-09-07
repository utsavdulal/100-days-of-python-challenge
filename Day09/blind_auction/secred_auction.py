# this program takes the input from users ($ they are willing to pay and once completed it discloses the winner)
import os
from art import logo
from clear_function import clear

print(logo)
print("Welcome to the secret auction program !")

bids = {}
bidding_over = True


def find_highest_bidder(bidding_record):
    # bidding_record = {"Utsav": 123, "James":400}
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid amount : ${highest_bid}")


while not bidding_over:
    name = input("Enter your name:")
    price = int(input("What is your bid ? $"))
    bids[name] = price
    should_continue = input("Are there other bidders type 'Yes' or 'No' :").lower()

    if should_continue == "no":
        bidding_over = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
