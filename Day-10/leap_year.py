# code to calculate if its a leap year or not


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                #   print(f"year {year} is a leap year")
                return True
            else:
                #   print(f"year {year} is NOT a leap year")
                return False
        else:
            # print(f"year {year} is a Leap year")
            return True
    else:
        # print(f"year {year} is NOT a leap year")
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return days_in_month[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
