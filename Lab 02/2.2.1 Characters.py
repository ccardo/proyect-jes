##
# the program prints out the first and last 3 characters
# of any string, disjointed by '...'
StringInput = input("insert any string: ")
convStr = str(StringInput)
strLength = len(convStr)

printOut = (convStr[0] + convStr[1] + convStr[2] + "..." + convStr[strLength - 3] +
            convStr[strLength - 2] + convStr[strLength - 1])
print(printOut)
