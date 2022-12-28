##
#   game of I'll kill you if you said what I said 10 minutes ago

def main():

    playing = True

    while playing:

        play()
        yn = input('Continue? (yes/no)')
        if yn.strip().lower().startswith("n"):
            playing = False


def play():

    words = list()
    last = input("Enter a word: ").strip().lower()
    words.append(last)

    validGame = True
    while validGame:
        # we are actually playing the game
        newWord = input("Insert a new word: ").strip().lower()

        if newWord == "*":
            validGame = False
            print("Quitting game...")

        elif len(newWord) < 2 or newWord[:2] != last[-2:]:
            validGame = False
            print("The word is not valid")
            print("Quitting game...")

        elif newWord in words:
            validGame = False
            print("Word has already been said")
            print("Quitting game...")

        else:
            words.append(newWord)
            last = newWord

main()
