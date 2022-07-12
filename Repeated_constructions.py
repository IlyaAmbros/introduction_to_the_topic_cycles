
PARKING_PLACES = 7
FREE_PLACE = 3

print("#"*PARKING_PLACES*5)

for place_index in range(1, PARKING_PLACES + 1):
    if place_index == FREE_PLACE :
        print("|   |", end="")
    else :
        print("| X |", end="")


print("\n","#"*PARKING_PLACES*5, sep="")

# The print() function; sep is a separator used between multiple values when printing.