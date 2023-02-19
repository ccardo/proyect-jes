import string
PUNCTUATION = string.punctuation

def main():

    with open("strawberry fields.txt") as file:
        text = [i.strip(PUNCTUATION) for i in file.read().upper().split()]

    for i, word in enumerate(text[:-2]):
        if len(word) == len(one_ahead:=text[i+1]) == len(two_ahead:=text[i+2]):
            print(word, one_ahead, two_ahead)

if __name__ == '__main__':
    main()
##