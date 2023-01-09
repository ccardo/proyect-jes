def main():

    filepath = "/Users/riccardo/VSCode Projects/proyect-jes/Exam exercises/Apple Pie/ApplePieRecipe.txt"
    with open(filepath, "r") as recipeFile:
        recipeLines = [i.strip().split() for i in recipeFile.readlines()]

    # save all lines in the instructions part --> index of the liene > index of "Instructions"
    importantLines = list()
    for i, line in enumerate(recipeLines):
        if i > recipeLines.index(["Instructions"]):
            importantLines.extend(line)

    filepath = "/Users/riccardo/VSCode Projects/proyect-jes/Exam exercises/Apple Pie/keyCode.txt"
    with open(filepath, "r") as keyCode:
        keys = keyCode.readline().strip()

    for key in keys:

        # apply the decoding criteria: word longer than 3 characters, first letter not the key letter
        for word in importantLines:
            if key in word and len(word) > 3 and word[0] != key:
                print(word[0], end="")


if __name__ == '__main__':
    main()
