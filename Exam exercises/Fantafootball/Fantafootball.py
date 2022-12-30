##
#

def get_players():

    from csv import reader

    playerList = list(reader(open("players.csv")))
    for i, player in enumerate(playerList):
        playerList[i] = list(map(str.strip, player))

    return playerList


def main():

    roles = {
        "goalkeeper": [3, 20],
        "defender": [8, 40],
        "midfielder": [8, 80],
        "forward": [6, 120]
    }

    players = get_players()
    for role in roles:

        print(role, end=" --> ")
        for i in range(roles[role][0], 0, -1):

            budget = roles[role][1] - i
            boughtPlayer = buy_player(role, budget, players)
            roles.update({role: [roles[role][0], budget + i - int(boughtPlayer[3])]})

            print(boughtPlayer[0], boughtPlayer[3], end=", ", sep=": ")

        print()


def buy_player(role: str, budget: int, playerList: list[list[str]]):

    playersRole = list(filter(lambda player: player[2] == role and budget > int(player[3]), playerList))
    try:
        boughtPlayer = playerList.index(max(playersRole, key=lambda i: int(i[3])))
        return playerList.pop(boughtPlayer)
    except IndexError:
        return print("Not enough money! Sorry :(")


main()