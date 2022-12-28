##
# this function simulates the PIN entering for an ATM
# if the PIN is incorrect three times in a row, the card is blocked
#

def main():
    CORRECTPIN = "1234"
    tries = 1
    limit = 3
    inputPIN = input('> Enter PIN: ')
    while CORRECTPIN:
        if inputPIN != CORRECTPIN:
            print(f'\nThe given PIN is incorrect. Try again.\n({limit - tries} more times)')
            tries += 1

        if tries == 4:
            exit("You have entered the wrong PIN 3 times.\nYour card has been blocked.")
        if inputPIN == CORRECTPIN:
            print("\n> Correct PIN. Access granted.")
            exit()
        inputPIN = input('> Enter PIN: ')


if __name__ == '__main__':
    main()
