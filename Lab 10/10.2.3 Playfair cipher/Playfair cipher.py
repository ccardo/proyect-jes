##
#
ALPHABET = "abcdefghiklmnopqrstuvwxyz"


def main():

    encryptionKey = input("insert an encryption key:\n>")
    with open("germano.txt", "r") as file:
        lines = file.readlines()
        lines = [i.split() for i in lines]

    words = list()
    for line in lines:
        words += line
    print(lines)

    for i, word in enumerate(words):
        if word.endswith(";"):
            word += "\n"
        words[i] = crypt(word, encryptionKey)

    poem = ""
    for i, word in enumerate(words):
        poem += f"{word} " if not word.endswith("\n") else f"{word}"

    with open("output.txt", "w") as output:
        output.write(poem)


def create_table(alphabet):
    table = list()
    for i in range(5):
        table += [[k for k in alphabet[5 * i: 5 * (i + 1)]]]

    return table


def clean_key(key):
    keySplit = [i for i in key]

    cleanKey = str()
    for i, k in enumerate(keySplit):
        if keySplit.index(k) < i:
            continue
        else:
            cleanKey += k

    return cleanKey


def encrypt_alphabet(key):
    alphabetTable = create_table(ALPHABET)
    key = clean_key(key)

    newAlphabet = list()
    for row in alphabetTable:
        newAlphabet += row

    for idx, letter in enumerate(key):
        newAlphabet.remove(letter)
        newAlphabet.insert(idx, letter)

    return create_table(newAlphabet)


def crypt(word, key):

    encryptedAlphabet = encrypt_alphabet(key)

    word = word.lower()
    lastLetter = word[-1] if len(word) % 2 and word.isalpha() else ""
    wordList = list()

    for k in range(0, len(word), 2):
        letterCouple = word[k:k+2]
        if not letterCouple.isalpha():
            wordList.append(letterCouple)
            continue
        if len(letterCouple) == 1:
            continue
        letterCouple = [i for i in letterCouple]

        coupleIndexes = dict()
        for char in letterCouple:
            for i, row in enumerate(encryptedAlphabet):
                if char in row:
                    j = row.index(char)
                    coupleIndexes.update({char: [i, j]})
                    break

        column1 = coupleIndexes[letterCouple[0]][1]  # essentially the x coordinates of the two characters are swapped
        column2 = coupleIndexes[letterCouple[1]][1]
        column1, column2 = column2, column1
        if column1 == column2:
            splitAlphabet = []
            for m in encryptedAlphabet:
                splitAlphabet += m
            swapped0 = splitAlphabet.index(letterCouple[1])
            swapped1 = splitAlphabet.index(letterCouple[0])
            letterCouple[0], letterCouple[1] = splitAlphabet[swapped0], splitAlphabet[swapped1]
        else:
            for idx, char in enumerate(letterCouple):
                for jdx, row in enumerate(encryptedAlphabet):
                    if char in row:
                        letterCouple[idx] = row[column1] if idx == 0 else row[column2]
                        break

        letterCouple = "".join(letterCouple)
        wordList.append(letterCouple)
    if lastLetter:
        wordList.append(lastLetter)
    crypted = "".join(wordList)

    return crypted

main()