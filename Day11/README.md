# Day 11 – Python Exercises

This folder contains Python scripts for Day 11 of the 100 Days of Python Challenge.

Day 11 focuses on **building a full Blackjack game** using functions, loops, conditional logic, and randomness.

## 📂 Files in this folder:

- **`blackjack.py`** – Main Blackjack game:

  - Imports ASCII art (`art.py`) and clear screen utility (`clear_function.py`).
  - Defines helper functions:

    - `deal_card()` – Returns a random card from the deck.
    - `calculate_score(cards)` – Calculates current hand score, handles Blackjack (Ace + 10) and Ace value conversion.
    - `compare(user_score, computer_score)` – Determines the winner based on game rules.

  - Simulates user and computer turns with score tracking.
  - Supports replaying multiple rounds in a loop.

- **`clear_function.py`** – Utility function to clear the terminal screen depending on the OS.

- **`art.py`** – Contains the ASCII art banner displayed at the start of the Blackjack game.

---

## 🃏 Game Rules:

- The deck contains numbers **2–10** and face cards (all counted as 10).
- **Ace (11)** can also be used as 1 if the hand goes over 21.
- Blackjack (Ace + 10) is represented with a score of **0** for easy comparison.
- The computer draws cards until it reaches a score of **17 or higher**.
- The player decides whether to **draw another card or pass**.

---

## ✨ Resources:

Here are the main resources I used to learn and practice Python on Day 11:

- [**Python Official Documentation**](https://docs.python.org/3/) – For working with lists, random, and functions.
- [**100 Days of Python Challenge by Udemy**](https://www.udemy.com/course/100-days-of-code/?couponCode=KEEPLEARNING) – Guided daily exercises and projects.
- [**ASCII Art Reference**](https://textart.sh/) – For creating and customizing banners for projects.
