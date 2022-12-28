##
#

def main():

    userFiles = input("Insert files, separated by a comma:\n>")
    files = [file.strip(", ") for file in userFiles.split()]
    print(files)

    Word = input("Insert word to search in these files:\n>")

    for file in files:

        with open(file, "r") as inFile:
            lines = inFile.readlines()
            for idx, line in enumerate(lines):
                lines[idx] = line.replace("â€™", "'")

            searchResult = list(filter(lambda x: Word in x, lines))
            print(f'\nFound word {Word} in "{file}":\n')
            for i, line in enumerate(searchResult):
                print(f'{i+1}. "{line}"')

if __name__ == '__main__':
    main()
