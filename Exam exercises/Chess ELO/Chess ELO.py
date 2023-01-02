##
#

def delta(player1, player2):
    return 1 / (1 + 2 ** ((player1 - player2) / 100))


def main():

    from csv import reader

    players = {}
    with open("players.csv") as file:
        data = [i.split(",") for i in file.readlines()]
        for line in data[1:]:
            players.update({line[0].strip(): int(line[1].strip())})         # create dict with name and ELO

    games = list(reader(open("games.csv")))[1:]
    for game in games:
        game.extend(game.pop(2).split("-"))                                 # split the score at the dash

    for game in games:

        for player in [game[0], game[1]]:                                   # update "players" with 1500 as ELO
            if player not in players:                                       # if the player is not in players
                players.update({player: 1500})

        elo0 = players[game[0]]
        elo1 = players[game[1]]
        elo_difference = 200 * round(delta(elo0, elo1))

        try:
            if int(game[2]) > int(game[3]):                                 # sees who won:
                elo0 = elo_difference                                       # except ValueError --> if the score
                elo1 = -elo_difference                                      # is 1/2 (tie), it raises ValueError
            elif int(game[2]) < int(game[3]):                               # and does nothing to the ELOs
                elo0 = -elo_difference
                elo1 = elo_difference
        except ValueError:
            continue

        players.update({game[0]: players.get(game[0]) + elo0})
        players.update({game[1]: players.get(game[1]) + elo1})

    # print the ELOs in descending order
    print(*sorted(players.items(), key=lambda x: x[1], reverse=True), sep="\n")


if __name__ == '__main__':
    main()
