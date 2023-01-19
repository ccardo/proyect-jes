#
from poker import hand_check, generate_deck
import time
#

counter = 0
done = False
while not done:

    counter += 1
    deck = generate_deck()
    #
    hands = []
    for i in range(0, len(deck) - 2, 5):
        hands.append(deck[i: i+5])

    for hand in hands:

        return_value = hand_check(hand)
        if return_value == "Royal Flush":
            print(*hand, sep="\n")
            print("Royal Flush!!!!")
            done =  True

for hand in hands:
        print()
        for card in hand:
            print(f"{card[0]} {card[1]}")

print(f"Count of decks processed : {counter}")
print(f"Process time in seconds : {time.process_time()}")