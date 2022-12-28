##
# the program prints out the digits of a 5-digit integer inserted by the user
a = int(input("input an integer, 5-digit number: "))
if 9999 < a < 100000:
    # the number is converted into a string; for every character in that string,
    # the program prints it out in a single line
    s = str(a)
    for i in s:
        print(i)
else:
    print(a, "is not a 5-digit number")
