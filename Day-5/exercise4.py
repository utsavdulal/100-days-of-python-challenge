# write a program that prints , fizz if divisible by 3, buzz if divisible by 5 and fizzbuzz if divisible by both
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FuzzBuzz !")
    elif number % 3 == 0:
        print("fuzz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
