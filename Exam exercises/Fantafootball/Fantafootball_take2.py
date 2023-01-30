##

def main():

    with open("players.csv") as csv_file:
        players = [i.strip().split(", ") for i in csv_file]

    budget = 200
    max_players_and_budget = {
        "goalkeeper": [3, 20],
        "defender": [8, 40],
        "midfielder": [8, 80],
        "forward": [6, 120]
    }

    roles = {i: [] for i in max_players_and_budget}
    for role in roles:
        roles[role] += [[i[0], int(i[3])] for i in players if i[2] == role]

    bought_players = {role: [] for role in roles}
    for role in max_players_and_budget:
        ranked_by_price = sorted(roles[role], key=lambda x: x[1], reverse=True)
        role_number, role_budget = max_players_and_budget[role]
        for player in ranked_by_price:
            cost = player[1]

            if cost <= role_budget and role_budget - cost >= role_number - 1:
                bought_players[role].append(player)
                role_budget -= cost
                role_number -= 1

            if len(bought_players[role]) >= max_players_and_budget[role][0]: break

    for role in bought_players:
        print(f"{role}:", end=' ')
        for player in bought_players[role]:
            print(*player, sep=" ", end=" ")
        print()


if __name__ == '__main__':
    main()