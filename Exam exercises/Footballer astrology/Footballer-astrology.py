##
#

def man():

    from csv import reader

    footballers = list(reader(open("footballers")))
    astrology = list(reader(open("astrology")))

    goals_by_zodiac_sign = {}

    for player in footballers:

        goals = int(player[1])
        birthday = int(player[3][:2]), int(player[3][3:5])

        for sign in astrology:

            # transform the dates into tuples to make comparison easier
            date_start = int(sign[1][:2]), int(sign[1][3:])
            date_end = int(sign[2][:2]), int(sign[2][3:])

            if (date_start[0] <= birthday[0] <= 31 or 1 <= birthday[0] <= date_end[0]) \
                    and (date_start[1] <= birthday[1] <= date_end[1]):

                # checks if the sign is already in the dict, if so: add the goals to that sign
                if sign[0] in goals_by_zodiac_sign:
                    goals_by_zodiac_sign[sign[0]] += goals
                else:
                    goals_by_zodiac_sign.update({sign[0]: goals})

                break

    # get the most goals and assign that to the longest line (50 asterisks)
    most_goals = max([goals_by_zodiac_sign.get(key) for key in goals_by_zodiac_sign])
    longest_line = 50
    for sign in goals_by_zodiac_sign:

        # print every other line proportionally
        goals_of_sign = goals_by_zodiac_sign[sign]
        line = (goals_of_sign / most_goals) * longest_line
        print(f"{sign:<15}{'*' * round(line)}")


if __name__ == '__main__':
    man()
