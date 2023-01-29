##
from csv import reader

def main():

    raw_astrology = list(reader(open("astrology")))
    footballers = list(reader(open("footballers")))

    zodiac_dates = {i[0]: i[1:] for i in raw_astrology}

    goals_by_sign = {sign: 0 for sign in zodiac_dates}
    for sign in zodiac_dates:

        day_start, month_start = map(int, zodiac_dates[sign][0].split("/"))
        day_end, month_end = map(int, zodiac_dates[sign][1].split("/"))

        for player in footballers:

            birth_date = player[3]
            birth_month = int(birth_date[3:5])
            birth_day = int(birth_date[:2])

            if birth_month == month_start and birth_day >= day_start:
                goals_by_sign[sign] += int(player[1])
            elif birth_month == month_end and 0 < birth_day <= day_end:
                goals_by_sign[sign] += int(player[1])

    # plot the n. of goals onto a histogram
    max_length = 50
    top_goals = sorted(goals_by_sign, key=goals_by_sign.get, reverse=True)
    best_sign = top_goals[0]
    for sign in top_goals:
        print(f"{sign:>15}", end=" ")
        print(f'{"*" * round((goals_by_sign[sign] / goals_by_sign[best_sign]) * max_length)}')


if __name__ == '__main__':
    main()