##
#

with open("marys_lamb.txt", "r") as marySong:
    textInput = marySong.readlines()
    lines = [i.strip().split() for i in textInput]

    uniqueWords = set()
    for i in lines:
        for j in i:
            j = j.lower()
            j = j.strip(',.')
            j = j.strip("'s")
            uniqueWords.add(j)

    for i, word in enumerate(sorted(uniqueWords)):
        print(f'{i+1}. {word}')

print('\nfinish')
