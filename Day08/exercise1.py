# program to calculate the number of can you need to paint the wall
import math


def paint_calc(height, width, cover):
    cover = (height * width) / coverage
    print(f"you need {math.ceil(cover)} cans to paint this wall")


# taking input from user
test_h = int(input("Height of wall: "))
test_w = int(input("width of wall "))
# coverage = the sq feet a can can cover
coverage = 5
# calling the above fucntion
paint_calc(height=test_h, width=test_w, cover=coverage)
