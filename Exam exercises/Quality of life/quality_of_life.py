##
from csv import reader


def main():

    city_statistics = list(reader(open("statistics.txt")))

    # save all the indicators in a dictionary and a list (list will be needed later to index.)
    indicators = {line[5]: {} for line in city_statistics[1:]}
    indicators_list = [i for i in indicators]
    print("\nQuality of life indicators:\n")
    for i, ind in enumerate(indicators):
        print(f"{i+1}) {ind}")

    # add every city to a dictionary ({city_name: value}) associated with each indicator
    for category in indicators:
        indicators[category] = group_by_indicator(category, city_statistics)
    
    # get the user input -> if it's not an integer, it means the user has input the indicator name directly
    try:
        user_input = input("Which indicator do you want to list the cities by?\n> ")
        search = indicators_list[int(user_input)-1]
    except ValueError:
        search = user_input
    except IndexError: search = -1
    if search not in indicators: exit("\nNo such indicator. Try again.")

    # sort the cities by the indicator chosen by the user
    print(f"Sorting cities by {search}")
    result = sorted(indicators[search], key=indicators[search].get, reverse=True)
    for city in result:
        print(f"{city:<25}{indicators[search][city]}")

def group_by_indicator(indicator, list) -> dict:
    return {city[3]: float(city[4]) for city in list if city[5] == indicator}

if __name__ == "__main__":
    main()