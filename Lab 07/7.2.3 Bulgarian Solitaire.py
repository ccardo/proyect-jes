##
#
def main():
    import random as rd
    import time
    deck, n = 45, 0                                             # 'deck' is the n. of starting cards
    cardPiles = []                                              # 'n' is the number of turns

    while deck > 0:
        pile = rd.randint(1, deck)
        deck -= pile
        cardPiles.append(pile)                                  # randomly generates the card piles
    print(f'Initial set of card piles: {cardPiles}\n')
    time.sleep(1)                                               # waits 1 s before starting to play

    while sorted(cardPiles) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        cardPiles = list(map(lambda x: x-1, cardPiles))         # subtract 1 from every pile
        newPile = len(cardPiles)
        while 0 in cardPiles:                                   # removes the empty piles
            cardPiles.remove(0)                                 # to prevent any zeros from showing up
        cardPiles.append(newPile)
        time.sleep(0.1)                                         # waits 0.1 seconds to make the move
        n += 1
        print(f'{n}{".":<4}', end="")
        print(*cardPiles, sep=", ")
    print(f'\nThe game was completed in {n} moves.')


main()
