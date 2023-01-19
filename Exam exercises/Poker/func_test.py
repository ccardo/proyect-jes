#
from poker import hand_check, generate_deck
import time
#
deck = generate_deck()
#
hands = []
for i, _ in enumerate(deck[:len(deck) - 2]):
    if i % 5:
        continue
    hands.append(deck[i: i+5])

done = False
while not done:

    for hand in hands:

        return_value = hand_check(hand)
        if return_value == "Royal Flush":
            print(hand)
            print("Royal Flush!!!!")
            done =  True

print(hands)
print(time.process_time())