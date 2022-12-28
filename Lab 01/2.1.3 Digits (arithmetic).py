##
# the program reads and prints out the digits of any 5-digit number
#
n = int(input("insert a five-digit integer: "))
if 9999 < n < 100000:
    x = 4
    #
    # the number will be divided by increasingly lower powers of 10, up to 0
    #
    while x >= 0:
        digit = n // (10 ** x)
        print(digit)
        #
        # the first digit will be removed and the program will go on
        #
        n = n - digit * (10 ** x)
        x = x - 1
else:
    print("the number must consist of 5 digits")
