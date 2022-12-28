##
#   literally the same program as 9.1.3 but
#   this time it actually works with negative numbers

# list input;
print("type QUIT to quit")
userInput = input("> enter integer: ")
integers = list()
while userInput.upper() != "QUIT":
    integers.append(float(userInput))
    userInput = input("> enter integer: ")

print("\nBAR GRAPH:\n")
greatest = max(map(abs, integers))
maxLength = 40

# handling negative numbers;
negatives = list(filter(lambda x: x < 0, integers))
smallest = min(negatives) if len(negatives) > 0 else 0

tabbing = abs(int(maxLength * smallest // greatest))

# printing graph
for num in integers:
    length = abs(int(maxLength * num // greatest))
    if num >= 0:
        print(f"{' ' * int(tabbing)}{'▄' * length}")
    else:
        print(f"{' ' * int(tabbing - length)}{'▄' * length}")
