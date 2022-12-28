##
#
ALPHABET = {i for i in "abcdefghijklmnopqrstuvwxyz"}


def main():

    string1 = input('Insert any string: ').lower()
    chars1 = {i for i in string1}

    string2 = input("Insert any other string: ").lower()
    chars2 = {i for i in string2}

    print(chars1 & chars2, end='\n\n')
    print(chars1 - chars2, end='\n\n')
    print(chars2 - chars1, end='\n\n')
    print(ALPHABET - chars1 - chars2)

main()
