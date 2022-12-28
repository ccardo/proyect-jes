##
#   this program is literally the same as program 9.1.3
#   but this time there are CAPTIONS!! to go along with the data

# list input;
print("type QUIT to quit")
captionInput = input("> enter caption: ")
userInput = input("> enter integer: ")
integers = list()
captions = list()
while userInput.upper() != "QUIT" or captionInput.upper() != "QUIT":
    integers.append(int(userInput))
    captions.append(captionInput)
    captionInput = input("> enter caption: ")
    userInput = input("\n> enter integer: ")

# handling preliminary information about the graph (max length, length of the longest caption)
print("\nBAR GRAPH:\n")
greatest = max(integers)
maxLength = 40
maxLengthCaption = max(map(len, captions))

# printing graph alongside captions
for idx, num in enumerate(integers):
    length = maxLength * num // greatest
    print(f"{captions[idx]:>{maxLengthCaption}}", end=' ')
    print("▄" * length)
