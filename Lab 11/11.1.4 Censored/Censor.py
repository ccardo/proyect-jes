##
#

def read_file(file):

    with open(file, "r") as infile:
        lines = infile.readlines()
    return lines


def main():

    with open("british-swear-words-list_text-file.txt", "r") as file:
        swearWords = set(map(str.strip, file.readlines()))

    lines = read_file("input.txt")

    with open("output.txt", "w") as output:

        for line in lines:
            for i in swearWords:
                if i in line:
                    line = line.replace(i, i[0]+"*"*(len(i)-1))
            output.write(line)

main()