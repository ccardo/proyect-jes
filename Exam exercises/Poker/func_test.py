#
from poker import hand_check, generate_deck
import time
#

royal_flush_counter = 0
deck_counter = 0
done = False
while not done:
    # for deck_counter in range(10**5):

    deck_counter += 1
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
            print(f"Current deck count: {deck_counter}")
            royal_flush_counter += 1
            done = True

"""for hand in hands:
        print()
        for card in hand:
            print(f"{card[0]} {card[1]}")"""

print(f"\nCounter of royal flushes: {royal_flush_counter}")
print(f"Count of decks processed : {deck_counter}")
print(f"Process time in seconds : {time.process_time()}")