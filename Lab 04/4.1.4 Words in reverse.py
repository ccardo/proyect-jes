##
# this program reads a word and outputs the word in reverse order
# and the uppercase letters in reverse order

stringInput = input('insert any string: ')
for i in range(len(stringInput) - 1, -1, -1):
    print(stringInput[i], end='')
print()
for i in range(len(stringInput) - 1, -1, -1):
    if stringInput[i].isupper():
        print(stringInput[i], end='')
