##
#   take the name of the team, display the count of unique players from that team

def main():
    with open("original_cards.txt", "r") as allPlayers:
        lines = allPlayers.readlines()
        uniquePLayers = {i.strip() for i in lines}                      # list of all cards (also duplicates)

        team = input('> insert desired team: ')
        counter = 0
        for card in uniquePLayers:
            if team in card:
                counter += 1
        print(F'{counter} players are in {team}.')

main()
