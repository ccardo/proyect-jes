##
def read_csv_into_dict(file):

    """stores every aminoacid as a key in a dictionary, and its associated codons in a list."""
    try:
        with open(file, "r") as infile:
            LINES = [i.strip().split(",") for i in infile.readlines()]
    except IOError and FileNotFoundError:
        exit("File format not correct, or file not existent.")

    my_dict = {}
    for line in LINES:
        for i, word in enumerate(line):
            line[i] = word.strip('" ')
        my_dict.update({line[0]: line[1:]})

    return my_dict


def main():

    from colorama import Fore, init
    init()  # activates colorama

    GENOME = read_csv_into_dict("codice_genetico.csv")
    START_CODONS = GENOME["start"]
    STOP_CODONS = GENOME["stop"]

    Sequence = input("Insert a sequence of codons: ").upper()
    NUCLEOTIDES = "ACGU"
    while not all(i in NUCLEOTIDES for i in Sequence):   # checks if all the characters are valid nucleotides
        Sequence = input(Fore.RED + "There are incorrect characters in the sequence. Try another time.\n>" + Fore.RESET)

    start_check = list(filter(lambda x: Sequence[x: x+3] in START_CODONS, range(len(Sequence))))       # checks for the
    start = start_check[0] if start_check else exit("No starting sequence was found.")  # presence of starting sequence

    stop = 0
    sequence_from_start = Sequence[start + 3:]          # checks for the presence of a stopping sequence
    for i in range(0, len(sequence_from_start), 3):     # after the start sequence
        currentCodon = sequence_from_start[i: i + 3]
        if currentCodon in STOP_CODONS:
            stop = (i + start + 3)                      # 'stop' is referred to the original sequence, so if found, it's
            break                                       # added to the length of the starting sequence and the start

    if not stop:
        exit("No stopping sequence was found.")

    protein = ""
    finalSequence = Sequence[:start]                    # save the characters before the start

    for i in range(start, stop+1, 3):

        currentCodon = Sequence[i: i+3]                 # currentCodon = sequence taken 3 letters at a time
        for aminoacid in GENOME:
            if currentCodon in GENOME[aminoacid]:

                finalSequence += F"{Fore.RED}{currentCodon}{Fore.RESET}" if i == start or i == stop else currentCodon
                protein += f"{aminoacid} "              # add aminoacids to the protein
                break

    finalSequence += Sequence[stop+3:]
    print(f"Codon sequence with highlighted ends: {finalSequence}")
    print(f"Aminoacid sequence: {protein}")

if __name__ == '__main__':
    main()
