##
#

def main():

    with open("deck.txt") as deck_file:
        deck = list(map(str.strip, deck_file))

    hand_1 = [card for i, card in enumerate(deck) if i % 2 == 1]
    hand_2 = [card for i, card in enumerate(deck) if i % 2 == 0]

    types = {"Rosso": 5, "Verde": 3,"Giallo": 1}
    
    total_turns = range(15)

    points_on_table = 0
    points_1, points_2 = 0, 0
    for turn in total_turns:

        card_1 = hand_1.pop(0)
        card_2 = hand_2.pop(0)

        print(f"\nTurn n. {turn + 1}:")
        print(f"Card from player 1: {card_1}")
        print(f"Card from player 2: {card_2}")

        points_on_table += types[card_1] + types[card_2]

        if types[card_1] > types[card_2]:
            hand_score = "Player 1 wins the turn!"
            points_1 += points_on_table
            points_on_table = 0
        
        elif types[card_1] < types[card_2]:
            hand_score = "Player 2 wins the turn!"
            points_2 += points_on_table
            points_on_table = 0
        
        else:
            hand_score = "Tie."
    
        print(f"Winner: {hand_score}")
        print(f"Score player 1: {points_1}")
        print(f"Score player 2: {points_2}")
    
    if points_1 > points_2:
        print(f"\nPlayer 1 wins! {points_1} points.")
    elif points_1 < points_2:
        print(f"\nPlayer 2 wins! {points_2} points.")
    else:
        print("Tie.")

if __name__ == "__main__":
    main()
