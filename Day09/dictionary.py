python_dictionary = {
    "utsav": "Hello i am utsav people gave me a nickname (dad)",
    "aabash": "Hello i am aabash and people know me as utsav's son",
    "pandey": "Hello i am pandey and i am utsav's elder son",
    "hanish": "Hello i am hanish and i am utsav's younger son",
}

# adding new item to a existing dictnary
python_dictionary["badal"] = "i am badal and i am utsav's step son"
# print(python_dictionary)

# wiping the above dictionary
# python_dictionary = {}
# print(python_dictionary)

# editing the existing dictionary
python_dictionary["hanish"] = "Hello i am hanish and i respect my dad (utsav)"
# print(python_dictionary)

for key in python_dictionary:
    # print(key)
    print(python_dictionary[key])
