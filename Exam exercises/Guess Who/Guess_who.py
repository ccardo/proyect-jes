##
#
def main():

    file_path = "characters.txt"
    file_path_input = input("> insert characters file name: ")
    file_path = file_path_input if file_path_input else file_path

    with open(file_path, "r") as file:
        people = [line.strip().split(";") for line in file]
        header = people[0][1:]

    characters = save_characters_data(people)

    # delete the header of the file after it is not needed
    del characters["Name"]

    # save either one of the question files
    question_file_1 = "questions1.txt"
    question_file_2 = "questions2.txt"
    with open(question_file_1) as file_input_1:
        questions1 = [line.strip().split(" = ") for line in file_input_1]

    # dictionary containing the characters matching the question
    matching_characters = match_questions(characters, questions1)

    # if there is only 1 person remaining at the end, you won; else, eat shit
    print("\nYou WON!") if len(matching_characters) == 1 else print("\nYou LOST!")


def save_characters_data(people_list: list):

    header = people_list[0][1:]

    # create a dictionary of dictionaries for storing the data of every character
    characters = {}
    for person in people_list:

        # characters[person[0]] = name of character
        # dictionary comprehension = "feature name": feature value for every character
        person_info = person[1:]
        characters[person[0]] = {header[i]: person_info[i] for i, _ in enumerate(header)}

    return characters


def match_questions(matching_characters: dict, questions: list) -> dict:

    CHARACTERS = matching_characters
    for question in questions:

        print()
        print(*question, sep=" --> ")

        feature, feature_value = question

        # filter the matching people by the question
        matches = list(filter(lambda person: matching_characters[person][feature] == feature_value, matching_characters))
        matching_characters = {person: CHARACTERS[person] for person in matches}

        for person in matching_characters:
            print(f"{person}:", *matching_characters[person].values())

    return matching_characters


if __name__ == '__main__':
    main()