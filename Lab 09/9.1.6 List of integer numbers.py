##
#   list of integer numbers all in ont input
#   separated by a colon
# display various things blaa bla babl

# inputting list
userInput = input("Input a series of integers, separated by colons (ex. 1:2:6:13)\n> ")
LIST = userInput.split(":")
LIST = list(filter(lambda x: x.isdigit(), LIST))
LIST = list(map(int, LIST))


# I) the input numbers, excluding the maximum and the minimum;
printable = LIST[::-1][::-1]
printable.remove(max(printable))
printable.remove(min(printable))
print("Numbers without maximum and minimum:")
print(*printable, sep=":")


# II) Among the inputted numbers, only the even values;
printable = LIST[::-1][::-1]
printable = [i for i in printable if i % 2 == 0]
print("Only even numbers:")
print(*printable, sep=":")


# III) Among the inputted numbers, only the 2-digit numbers;
printable = LIST[::-1][::-1]
printable = list(map(str, printable))
printable = [i for i in printable if len(i) == 2]
print("Only 2-digit values:")
print(*printable, sep=":")
