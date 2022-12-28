##
#   this program receives a sequence of input values and
#   displays proportionally long bars (max len = 40)

# list input;
print("type QUIT to quit")
userInput = input("> enter integer: ")
integers = list()
while userInput.upper() != "QUIT":
    integers.append(int(userInput))
    userInput = input("> enter integer: ")

print("\nBAR GRAPH:\n")
greatest = max(integers)
maxLength = 40

# printing graph
for num in integers:
    length = maxLength * num // greatest
    print("▄" * length)
