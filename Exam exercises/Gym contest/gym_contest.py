##


def main():

    with open("scores.txt") as file:
        contestants = [i.strip().rsplit(maxsplit=7) for i in file]

    for contestant in contestants:
        score = list(map(float, contestant[3:]))
        contestant.remove(str(min(score)))
        contestant.remove(str(max(score)))

    # noinspection PyTypeChecker
    female_scores = {i[0]: i[1:3] + [sum(map(float, i[3:]))] for i in contestants if i[1] == "F"}

    scores_by_nationality = {i[2]: 0.0 for i in contestants}
    for participant in contestants:

        nationality = participant[2]
        score = participant[3:]

        scores_by_nationality[nationality] += round(sum(map(float, score)), 2)

    # pick out the best girly girl omg
    top_female_contestant = max(female_scores, key=lambda x: female_scores[x][2])
    nationality = female_scores[top_female_contestant][1]
    score = female_scores[top_female_contestant][2]
    print(f"Female champion -> {top_female_contestant}, {nationality} - {score} points")

    # rank the top 3 nations based on sexiness omg
    for i, nation in enumerate(sorted(scores_by_nationality, key=scores_by_nationality.get, reverse=True)[:3]):
        print(f"{i+1}) {nation} - {scores_by_nationality[nation]} points")

if __name__ == '__main__':
    main()