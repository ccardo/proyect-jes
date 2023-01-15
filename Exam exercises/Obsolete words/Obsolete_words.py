##
#
import string
from pprint import pprint


def main():

    # create dictionary of obsolete words
    with open("obsolete.txt") as obsolete_file:
        lines = [i.split() for i in obsolete_file]
    
    obsolete_words = {line[0]: line[1] for line in lines}

    with open("text.txt") as file_text:
        text = file_text.read().split()

    sub_count = {obs_word: 0 for obs_word in obsolete_words}
    for obs_word in obsolete_words:

        for idx, word in enumerate(text):

            if obs_word == word.strip(string.punctuation):

                text[idx] = obsolete_words[obs_word]
                sub_count[obs_word] += 1

    print("Obsolete word count:\n")
    pprint(sub_count)
    with open("output.txt", "w") as out_file:
        for word in text:
            out_file.write(f"{word} ")

main()