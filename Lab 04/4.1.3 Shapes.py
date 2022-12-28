##
#
sideLength = int(input('Side length: '))

# square code
for x in range(sideLength):
    print('*  ' * sideLength)
print()

# rhombus code
diagonal = 2 * sideLength

for row in range(1, diagonal):

    spaces = abs(sideLength - row)
    asterisks = 2 * sideLength - 1 - (2 * spaces)

    for i in range(spaces):  # prints the amount of empty spaces
        print(end='  ')
    for j in range(asterisks):  # prints the amount of asterisks per row
        print('* ', end='')
    print()  # prints a new line when the row is done
