import string
PUNCTUATION = string.punctuation

def main():

    with open("strawberry fields.txt") as file:
        text = [i.strip(PUNCTUATION) for i in file.read().upper().split()]

    for i, word in enumerate(text[:-2]):
        if len(word) == len(text[i+1]) == len(text[i+2]):
            print(word, text[i+1], text[i+2])

if __name__ == '__main__':
    main()
