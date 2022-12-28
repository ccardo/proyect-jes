##
#
def main():
    from csv import reader

    year = input("From what year do you want to gather data? (2004 or 2021): ").strip(",/;:'")

    if year == "2021":
        with open("rawdata_2021.csv", "r") as file:
            lines = list(reader(file))
            lines.pop(0)

    elif year == "2004":
        with open("rawdata_2004.txt", "r") as file:
            lines = [i.strip().split() for i in file.readlines()]
            for line in lines:
                line.pop(0)
                index = 1
                while line[index].isalpha():
                    line[index-1] = " ".join([line[index-1], line[index]])
                    line.pop(index)
    else:
        exit("No data from input year. Try again.")

    user_search = input("insert name of country: ").lower().strip(",/;:'")
    search_result = list(filter(lambda x: user_search in x[0].lower(), lines))
    if not search_result:
        exit("Country not found. It's possible you typed the name wrong. Try again.")

    if year == "2021":
        print(search_result[0][0], search_result[0][2], sep=' - ')
    else:
        print(search_result[0][0], f"${search_result[0][2]}", sep=" - ")

if __name__ == '__main__':
    main()