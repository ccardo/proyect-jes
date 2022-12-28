##
#

def save_file_as_words(file):

    with open(file, "r") as infile:
        lines = map(str.strip, infile.readlines())

    special_chars = ".,><:;!?/'\""
    lines = list(map(str.split, lines))
    words = list()
    for line in lines:
        for word in line:
            word = word.strip(special_chars).lower()
            words.append(word)
    return words


if __name__ == '__main__':

    glossary = dict()
    word_list = save_file_as_words("input.txt")

    for word in word_list:
        if word not in glossary:
            glossary.update({word: 1})
        else:
            glossary[word] = glossary.get(word) + 1

    for key in sorted(glossary):
        print(f"{f'{key.capitalize()}:':<11}{glossary.get(key):>5}")
