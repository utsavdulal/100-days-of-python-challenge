# # simple function
# def greet():
#     print("My name is utsav dulal")
#     print("i am from itahari")
#     print("i am 22 years old")
# greet()


# # function that accepts input
# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"how are you mr.{name}")
#     print(f"hey {name} how old are you")
# greet_with_name("Utsav")


def greet_with(name, location):
    print(f"Hey {name}")
    print(f"what is it like in {location}")


# postional argument
# greet_with("utsav", "nepal")

# keyword argument
greet_with(location="nepal", name="utsav")
