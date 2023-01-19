##
#
from random import shuffle

card_values = {
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def generate_deck():

    VALUES = ["7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["c", "q", "f", "p"]

    _deck = [(value, suit) for value in VALUES for suit in SUITS]
    shuffle(_deck)

    return _deck


def main():

    deck = generate_deck()

    with open("mazzo.txt", "w") as output:
        [output.write(f"{card[0]} {card[1]}\n") for card in deck]
    
    hands = []
    for i in range(0, len(deck) - 2, 5):
        hands.append(deck[i: i+5])

    for hand in hands:
        print()
        for card in hand:
            print(f"{card[0]} {card[1]}")
        print(hand_check(hand))


def hand_check(_hand):

    hand_values = [card_values[card[0]] for card in _hand]
    hand_suits = [card[1] for card in _hand]
    value_range = range(min(hand_values), max(hand_values) + 1)

    if len(set(hand_suits)) == 1:
        if hand_values == [i for i in value_range]:
            return "Royal Flush"

    elif any(hand_values.count(value) == 4 for value in hand_values):
        return "Four of a kind"
    
    elif len(set(hand_suits)) == 1:
        return "Flush"

    elif len(set(hand_values)) == 2:
        return "Full House"
    
    elif hand_values == [i for i in value_range]:
        return "Straight"

    elif any(hand_values.count(value) == 3 for value in hand_values):
        return "Three of a kind"
    
    counter = set()
    for value in hand_values:
        if hand_values.count(value) == 2:
            counter.add(value)
    if len(counter) == 2:
        return "Double Pair"
    
    elif len(set(hand_values)) == 4:
        return "Pair"

    else:
        return "No combinations."


if __name__ == "__main__":
    main()
