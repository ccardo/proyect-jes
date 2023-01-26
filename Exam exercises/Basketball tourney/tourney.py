##
#

def main():

    with open("games.txt") as input_file:
        games_raw = [line.strip().split(" : ") for line in input_file]
    games = []
    for line in games_raw:
        game = line[0].split(" - ")
        game.extend(list(map(int, line[1].split(" - "))))
        games.append(game)

    teams_info = {}
    for game in games:
        teams_info[game[0]], teams_info[game[1]] = [0, 0, 0, 0], [0, 0, 0, 0]

    for game in games:
        team_1, team_2, score_1, score_2 = game

        if game[2] > game[3]:
            teams_info[team_1][1] += 3
            teams_info[team_2][1] += 1

        elif game[3] > game[2]:
            teams_info[team_1][1] += 1
            teams_info[team_2][1] += 3
        else:
            teams_info[team_1][1] += 2
            teams_info[team_2][1] += 2

        # times played
        teams_info[team_1][0] += 1
        teams_info[team_2][0] += 1
        # undergone scores
        teams_info[team_1][3] += score_2
        teams_info[team_2][3] += score_1
        # scores scored hahahaha
        teams_info[team_1][2] += score_1
        teams_info[team_2][2] += score_2
        # kd ratio hahahhaa

    for team in teams_info:

        score_undergone = teams_info[team][3]
        score_done = teams_info[team][2]

        teams_info[team].insert(2, round(score_done/score_undergone, 2))


    top_teams = sorted(teams_info, reverse=True, key=lambda x: teams_info[x][1])
    for i, team in enumerate(top_teams[:-1]):

        team1_info = teams_info[team]
        team2_info = teams_info[top_teams[i+1]]
        if team2_info[1] == team1_info[1]:

            kd_1 = team1_info[2]
            kd_2 = team2_info[2]

            if kd_2 > kd_1:
                top_teams.insert(i, top_teams.pop(i+1))

    print(f"{'TEAMS':<25}{'GAMES':<10}{'SCORE':<7}{'KD':<7}{'PF':<5}{'PS'}")
    print("-"*56)
    for team in top_teams:
        games, score, kd, pf, ps = teams_info[team]
        print(f"{team:<25}{games:<10}{score:<7}{kd:<7}{pf:<5}{ps}")


if __name__ == '__main__':
    main()
