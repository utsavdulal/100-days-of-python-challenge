# importing ascii art from another folder called art.py
from art import logo

# list of alphabets
alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
print(logo)


# function to encode and decode the message
def caesar(user_message, secret_code, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        secret_code *= -1
    for char in user_message:
        if char in alphabets:  # if there is characters in user msg the encode / decode
            position = alphabets.index(char)
            new_position = position + secret_code
            cipher_text += alphabets[new_position]
        else:  # if there is no characters than print them as it is eg. hello505  decoded msg = mjqqt505
            cipher_text += char
    print(f"Your {cipher_direction}d message is : {cipher_text}")


should_continue = True
while (
    should_continue
):  # asking user if they want to continue tho use this program or exit
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Enter your message \n").lower()
    shift = int(input("Enter the shift number:\n"))
    shift = shift % 26  # used when user enters the larger number

    caesar(
        user_message=message, secret_code=shift, cipher_direction=direction
    )  # calling the above

    result = input("Type 'Yes' if you want to continue . Otherwise Type'No'").lower()
    if result == "no":
        should_continue = False
        print("Goodbye!")
