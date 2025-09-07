# Functions with outputs
def format_name(f_name, l_name):
    """using docstring:
    docstring :
    i am utsav dulal and i am from itahari sunsari i am the recent graduate of sushma koirala memorial engineering college
    """
    if f_name == "" or l_name == "":
        return "Please provide a valid input !"
    formatted_f_naems = (
        f_name.title()
    )  # .title() sunction is used to format any input into formatted like input :UtsaV , Output will be : Utsav
    formatted_l_name = l_name.title()
    return f"{formatted_f_naems} {formatted_l_name}"


print(format_name(input("What is your first name?"), input("what is your last name?")))

# name = input("Enter your name : ").title()
# print(name)
