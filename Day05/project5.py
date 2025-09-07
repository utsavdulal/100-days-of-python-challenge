import random
import string


letter = list(string.ascii_lowercase + string.ascii_uppercase)
number = list(string.digits)
symbol = list(string.punctuation)


user_letter = int(input("How many letters do you want ?"))
user_number = int(input("How many number do you want ?"))
user_symbol = int(input("How many symbols do you want ?"))

password_list = []

for _ in range(1, user_letter + 1):
    password_list.append(random.choice(letter))
for _ in range(1, user_number + 1):
    password_list.append(random.choice(number))
for _ in range(1, user_symbol + 1):
    password_list.append(random.choice(symbol))

random.shuffle(password_list)
random_password = " ".join(password_list)
print(random_password)
