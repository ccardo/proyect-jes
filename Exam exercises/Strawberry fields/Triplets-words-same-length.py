##
#

def main():

    # create a list with every single word in it
    with open("strawberry fields.txt", "r") as file:
        words = list()
        for line in file.readlines():
            words += [i.strip(",. ") for i in line.split()]

    # checks for triplets of same-length words
    for i, word in enumerate(words[:-2]):
        if len(word) == len(words[i+1]) == len(words[i+2]):
            print(f"{word, words[i+1], words[i+2]}".upper())


if __name__ == '__main__':
    main()
