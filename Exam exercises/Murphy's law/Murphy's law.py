##
#

def main():

    with open("murphy_reads.txt") as murphy_file:
        lines = [i.strip() for i in murphy_file]

    murphy_laws = {}
    header = ""
    for i, line in enumerate(lines[:-1]):

        if i == 0 or lines[i-1] == "":
            header = line
            murphy_laws[header] = ""

        if line == "":
            continue
        elif line is not header:
            murphy_laws[header] += f"{line} "

    with open("topics.txt", "r", encoding="utf8") as topics_file:
        topics = [i.strip() for i in topics_file]

    laws = list()
    for topic in topics:
        for law in murphy_laws:

            if topic in murphy_laws[law] and law not in laws:
                laws.append(law)

    for law in laws:
        print("\n", law, murphy_laws[law], sep=" - ")

if __name__ == '__main__':
    main()