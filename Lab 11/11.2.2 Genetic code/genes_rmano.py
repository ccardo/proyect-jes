##
#
def main():

    from csv import reader
    from colorama import Fore, init
    init()  # initializes colorama
    start, stop = None, None                                            # initializes the variables

    genes = {}                                                          # creates a dictionary;
    with open("codice_genetico.csv", "r") as file:                                # for every line in the CSV file,
        lines = list(reader(file))                                      # the program updates the dictionary
        #                                                               # with:
        for line in lines:                                              # {aminoacid : [codons]}
            genes.update({line[0]: line[1].split(", ")})

    START = genes["start"]
    STOP = genes["stop"]

    Sequence = input("input an RNA sequence:\n>").upper()               # inputs the sequence and checks if it's
    while not all(i in "AGCU" for i in Sequence):                       # all composed by valid characters
        Sequence = input(f"{Fore.RED}There are incorrect characters in the sequence. Try again.\n>{Fore.RESET}")

    try:    # saves the start of the coding sequence; if no starting seq., the list is empty, will raise an error
        start = list(filter(lambda x: Sequence[x: x+3] in START, range(len(Sequence))))[0]
    except IndexError:
        quit("No starting sequence found.")

    try:    # saves the end of the coding sequence; same thing with the empty list as above
        stop = list(filter(lambda x: Sequence[x: x + 3] in STOP, range(start, len(Sequence), 3)))[0]
    except IndexError:
        quit("No stopping sequence found.")

    genome = ""
    highlighted_sequence = Sequence[:start]
    for i in range(start, stop + 1, 3):

        try:    # adds the aminoacid, corresponding to the codon, to the genome. If none correspond, pass
            genome += f"{list(filter(lambda seq: Sequence[i: i + 3] in genes[seq], genes))[0]} "
        except IndexError:
            pass

        codon = Sequence[i: i + 3]
        if i == start or i == stop:                                     # highlights the start and end points
            codon = f"{Fore.RED}{codon}{Fore.RESET}"                    # of the sequence by coloring them red
        highlighted_sequence += codon

    highlighted_sequence += Sequence[stop + 3:]                         # adds the remaining characters, if any
    print(f"Sequence of aminoacids: {genome}")
    print(f"Sequence: {highlighted_sequence}")


if __name__ == '__main__':
    main()