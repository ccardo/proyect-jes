##
#

def get_instructions():

    with open("ApplePieRecipe.txt", "r") as file:
        lines = [i.strip() for i in file.readlines()]

    instr = list(filter(lambda line: lines.index(line) > lines.index("Instructions"), lines))
    instr = list(map(lambda x: x.split(), instr))
    instructions = list()
    for i in instr:
        instructions.extend(i)

    return instructions


def decode():

    with open("keyCode.txt", "r") as file:
        key = file.readline().strip()

    word = list()
    text = get_instructions()
    for i in key:
        letters = list(filter(lambda x: i in x and len(x) > 3 and x[0] != i, text))
        word.append(list(map(lambda x: x[0], letters)))

    return word


def main():

    wordList = decode()
    decoded = ""
    for i in wordList:
        for j in i:
            decoded += j

    print(decoded)

if __name__ == '__main__':
    main()