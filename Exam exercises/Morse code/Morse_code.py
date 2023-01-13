##
#

def main():

    with open("morse_code.txt") as morse_source:
        lines = [line.strip().split() for line in morse_source]

    # create two different dictionaries to use for translation
    text_to_morse = {line[0]: line[1] for line in lines}
    morse_to_text = {line[1]: line[0] for line in lines}

    # open a file according to the mode set by the user
    mode = int(input("INPUT\n1) From text to morse code;\n2) From morse to text.\n> "))
    filename = "my_text.txt" if mode == 1 else "my_text_2.txt"
    with open(filename) as text_input_file:
        text_input = [i.strip() for i in text_input_file]

    mode, text = text_input[0], " ".join(text_input[1:])            # header of file = mode;
    if mode == "C":                                                 # rest of file = text to translate
        translate_text_to_morse(text, text_to_morse)

    else:
        translate_morse_to_text(text, morse_to_text)


def translate_text_to_morse(text, dictionary):                      # translate text into morse code
    for letter in [i for i in text if i != " "]:                    # by translating each letter (no whitespaces)
        print(dictionary[letter], end=" ")


def translate_morse_to_text(morse_code, dictionary):                # translate morse code into text
    for letter in morse_code.split():                               # by analyzing each group of morse characters
        print(dictionary[letter], end=" ")


if __name__ == '__main__':
    main()
