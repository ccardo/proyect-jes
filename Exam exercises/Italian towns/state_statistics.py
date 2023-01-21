##
#

def main():

    with open("towns.csv") as input_file:
        towns = [line.strip().split(";") for line in input_file]

    regions = {"Lazio": [], "Piemonte": []}
    for region in regions:
        
        print(f"\n{region}:")
        regions[region] = [town[6] for town in towns if town[10] == region]
        print(f"number of towns in {region}: {len(regions[region])}")

        names_by_len = sorted(regions[region], key=len)
        shortest_names = sorted(list(filter(lambda name: len(name) == len(names_by_len[0]), names_by_len)))
        print(f"Shortest town name: {shortest_names[0]}")

        longest_names = sorted(list(filter(lambda name: len(name) == len(names_by_len[-1]), names_by_len)))
        print(f"Longest town name: {longest_names[0]}")

if __name__ == "__main__":
    main()