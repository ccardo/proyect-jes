##
#

def get_players():

    """returns a list of the players in the file"""

    from csv import reader

    playerList = list(reader(open("players.csv")))
    for i, player in enumerate(playerList):
        playerList[i] = list(map(str.strip, player))

    return playerList


def main():

    # "role": [number of players, budget in millions]
    roles = {
        "goalkeeper": [3, 20],
        "defender": [8, 40],
        "midfielder": [8, 80],
        "forward": [6, 120]
    }

    players = get_players()
    for role in roles:

        print(role, end=" --> ")

        for i in range(roles[role][0] - 1, -1, -1):
            budget = roles[role][1]
            budget = budget - i
            boughtPlayer = buy_player(role, budget, players)
            roles.update({role: [roles[role][0], budget + i - int(boughtPlayer[3])]})

            print(boughtPlayer[0], boughtPlayer[3], end=", ", sep=": ")

        print()


def buy_player(role: str, budget: int, playerList: list[list[str]]):

    """skims the players to see the ones of the given role,
    then removes the player from the dictionary if bought"""

    players_of_that_role = list(filter(lambda player: player[2] == role and budget >= int(player[3]), playerList))
    try:
        boughtPlayer = playerList.index(max(players_of_that_role, key=lambda i: int(i[3])))
        return playerList.pop(boughtPlayer)
    except IndexError:
        return print("Not enough money! Sorry :(")


main()