##
#
def main():

    # opens and reads the file
    file_path = "Exam exercises/Bowling/bowling.txt"
    with open(file_path, "r") as file:
        lines = [line.strip().split(";") for line in file]
    
    # saves the name and the list of scores into a dictonary
    scores = {" ".join(player[:2]): player[3:] for player in lines}

    # uses the return_score function to compute the total scores
    total_scores = {name: return_total(scores[name]) for name in scores}
    ranking = sorted(total_scores, key=total_scores.get, reverse=True)
    for player in ranking:

        print(player, total_scores[player], sep=": ")
    
    # checks the count of each of the tracked numbers, returns the player with max. count
    print("\nMost 10s and most 0s:")
    for tracked_score in ["10", "0"]:

        count_of_tracked_score  = {name: scores[name].count(tracked_score) for name in scores}
        most_of_tracked_score = max(count_of_tracked_score, key=count_of_tracked_score.get)

        print(most_of_tracked_score, scores[most_of_tracked_score], sep=": ")

    

def return_total(list_of_scores):

    """returns the sum of the scores after transorming them into integers"""

    scores = map(int, list_of_scores)

    return sum(scores)

main()