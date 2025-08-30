#where do you want to hide a treasure map ?
row1= ["🔳", "🔳", "🔳"]
row2= ["🔳", "🔳", "🔳"]
row3= ["🔳", "🔳", "🔳"]
map = (row1, row2, row3)
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to hide a Treasure ?\n")

######################################################################

hor =int(position[0]) -1
ver =int(position[1]) -1
map [hor][ver] ="💰"
######################################################################
#printing the final map
print(f"{row1}\n{row2}\n{row3}")