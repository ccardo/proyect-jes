##
# this program displays the number of ticket buyers
# starting from a total of 100 tickets and with a max. of 4 tickets per purchase.

def main():
    tickets = 100
    buyers = 0
    while tickets > 0:
        purchase = int(input("> How many tickets will you buy? (max: 4) "))
        if purchase <= 4:
            tickets -= purchase
            print(f'\nThere are {tickets} tickets left.')
            buyers += 1
        else:
            print(f'The purchase is at most of 4 (four) tickets. Buy less next time!')

    print(f'The amount of buyers was: {buyers}')


if __name__ == '__main__':
    main()
