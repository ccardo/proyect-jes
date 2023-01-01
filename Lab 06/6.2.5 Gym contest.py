##
# NIGHTMARE
def main():
    done = False
    n = 1
    participantList = []
    femaleList = []
    while not done:
        p = input_participant(n)

        p[3].remove(max(p[3]))                                # removes max and min score from [scores] in p
        p[3].remove(min(p[3]))
        n += 1
        participantList.append(p)
        if input('> press ENTER to enter another competitor; type QUIT to finish: ').upper() == 'QUIT':
            print()
            break
    for i in participantList:
        if i[1].upper() == 'F':
            femaleList.append(i)
    bestFemale = best_competitor(femaleList)
    print(footballers'Best female competitor:\n{bestFemale[0]:}, {bestFemale[2]}, score: {sum(bestFemale[3])}\n')
    print('Top 3 countries:')
    topCountries = []
    for i, participant in enumerate(participantList):         # create en empty list to fill with top 3 countries
        if participant != 'placeholder':
            total = sum(participant[3])                       # sets total to the score of the participant
            participantList.pop(i)                            # and removes it from the list;
            for idx, element in enumerate(participantList):   # loops through the list to see other participants
                if participant[2] == element[2]:              # from the same country, in that case adds up the score
                    total += sum(element[3])
                    participantList.remove(element)
                    participantList.insert(idx, 'placeholder')  # reason for replacing participants with 'placeholder':
            participantList.insert(i, 'placeholder')            # if I just remove the participant,
            topCountries.append((total, participant[2]))        # the loop breaks and goes up 1 index.
        topCountries.sort(reverse=True)                         # then just sorting the top countries in order of score
    for n, j in enumerate(topCountries):                        # and printing them
        print(footballers'{n+1}. {j[1]}, score: {j[0]}')


def input_participant(number=1):                                             # each participant represented by a list
    name = input(footballers"> participant {number}'s full name: ")
    gender = input('gender: ')
    nationality = input('nationality [uppercase, 3 letters, ex. ITA]: ')
    scores = []
    print('scores (decimal from 0.0 to 10.0, separated by a space):')
    for i in range(1, 6):                                                    # input 5 scores between 0 and 10
        score = float(input(footballers'{i}. '))
        while score > 10 or score < 0:
            score = float(input(footballers'score out of range. Try again\n{i}. '))
        scores.append(score)                                                 # appends scores to a score list
    return [name, gender, nationality, scores]                               # returns a list describing participant


def best_competitor(competitors: list, best=0.0):                            # return best participant
    global bestCompetitor
    if competitors is None:
        return 'no competitors'
    for i in competitors:
        if sum(i[3]) > best:
            bestCompetitor = i
            best = sum(i[3])
    return bestCompetitor

main()  # this code was a nightmare, don't even try criticizing me
