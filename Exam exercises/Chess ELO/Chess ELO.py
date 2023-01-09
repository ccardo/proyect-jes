##
#

def delta(player1, player2):
    return 1 / (1 + 2 ** ((player1 - player2) / 100))


def main():

    from csv import reader

    with open("players.csv") as file:
        data = [i.split(",") for i in file.readlines()][1:]
        players = {line[0]: int(line[1]) for line in data}                  # create dict with name and ELO

    games = list(reader(open("games.csv")))[1:]                             # split the score at the dash

    for game in games:

        first_player, second_player = game[:2]
        for player in [first_player, second_player]:                        # update "players" with 1500 as ELO
            if player not in players:                                       # if the player is not in players
                players.update({player: 1500})

        elo_first = players[first_player]
        elo_second = players[second_player]
        elo_difference = round(200 * delta(elo_first, elo_second))

        elo0 = elo_difference if game[2] == "1-0" else -elo_difference
        elo1 = -elo0

        players[game[0]] += elo0
        players[game[1]] += elo1

    # print the ELOs in descending order
    print(*sorted(players.items(), key=lambda x: x[1], reverse=True), sep="\n")


if __name__ == '__main__':
    main()
