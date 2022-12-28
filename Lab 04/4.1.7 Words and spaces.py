##
#

def main():

    string = input("insert any string:\n>")

    substrings = list()
    for start, _ in enumerate(string):

        for end in range(start, len(string)):

            substrings.append(string[start:end+1])

    print(*sorted(substrings, key=len), sep="\n")

if __name__ == '__main__':
    main()