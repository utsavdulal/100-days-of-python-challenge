#code to calculate if its a leap year or not
print("Welcome to leap year calculator app")

year = int(input("Enter a year: \n"))

# if year % 4 ==0 :
#     print(f"year {year} is a leap year")
# elif year % 100 ==0:
#     print(f"year {year} is a not aleap year")
# elif year % 400 ==0:
#     print(f"year {year} is a leap year")
# else:
#     print(f"year {year} is not a leap year")


if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 ==0:
          print(f"year {year} is a leap year")
      else:
          print(f"year {year} is NOT a leap year")
    else:
        print(f"year {year} is a Leap year")
else:
    print(f"year {year} is NOT a leap year")    