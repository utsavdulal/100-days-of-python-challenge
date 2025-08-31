############# write a program to add all the even numbers form 1 to 100 #############
evens = 0
for number in range(0, 101, 2):
    evens += number
print(f"The sum of even numbers form 1 to 100 is : {evens}")
