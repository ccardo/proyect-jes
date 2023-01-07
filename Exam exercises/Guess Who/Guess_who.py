##
#
def main():

    file_path = "characters.txt"
    file_path_input = input("> insert characters file name: ")
    file_path = file_path_input if file_path_input else file_path

    with open(file_path, "r") as file:

        lines = [line.strip().split(";") for line in file]

    # create a dictionary of dictionaries for storing the data of every character
    characters = {}
    for line in lines:

        # characters[line[0]] = name of character
        # dictionary comprehension = "feature name": feature value for every character
        characters[line[0]] = {lines[0][i+1]: line[i+1] for i, _ in enumerate(lines[0][1:])}

    # delete the header of the file after it is not needed
    del characters["Name"]

    # save either one of the question files
    question_file_1 = "questions1.txt"
    question_file_2 = "questions2.txt"
    with open(question_file_1) as file_input_1:
        questions1 = [line.strip().split(" = ") for line in file_input_1]

    # temporary dictionary that will be modified, contains the characters matching the question
    matching_characters = characters

    for question in questions1:

        print()
        print(*question, sep=" --> ")

        feature = question[0]
        feature_value = question[1]

        # filter the matching people by the question
        matches = list(filter(lambda person: matching_characters[person][feature] == feature_value, matching_characters))
        matching_characters = {person: characters[person] for person in matches}

        for person in matching_characters:
            print(f"{person}:", *matching_characters[person].values())

    # if there is only 1 person remaining at the end, you won; else, eat shit
    print("\nYou WON!") if len(matching_characters) == 1 else print("\nYou LOST!")


if __name__ == '__main__':
    main()