import time


def main():                                         # main
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    printTable(table=board)                         # sets an initial board with numbers in place of blank spaces
    maxTurns = 8
    for turn in range(maxTurns):                    # alternates between even (X) and odd (O) turns
        if turn % 2 == 0:
            playerMove(board, 'O')
        else:
            playerMove(board, 'X')

        printTable(table=board)
        time.sleep(0.5)
        if winCheck(board, 'X') == 1:
            exit('\nPlayer X won!')
        if winCheck(board, 'O') == 1:
            exit('\nPlayer O won!')
    print('\nThe game ends in a tie!')


def winCheck(table: list, XorO: str):               # winCheck (3 equal symbols in a line)

    winVertical, n = [], 0                          # vertical sets of Xs or Os
    winDiagonal1, winDiagonal2 = [], []             # diagonal sets of Xs or Os
    for index, List in enumerate(table):
        winDiagonal1.append(List[index])            # diagonal of the table: each row on the (row)th index
        winDiagonal2.append(List[::-1][index])      # and in reverse for the opposite diagonal

        for Lst in table:
            winVertical.append(Lst[n])              # for each loop it's equal to the nth index of each row
        if winVertical.count(XorO) == 3:
            return 1
        if List.count(XorO) == 3:
            return 1

        winVertical.clear()
        n += 1
    if winDiagonal1.count(XorO) == 3:               # if the count of Xs or Os is equal
        return 1                                    # to the length of the list, then the list is full
    if winDiagonal2.count(XorO) == 3:
        return 1


def printTable(table: list):                                                    # printTable
    rows = len(table)
    columns = len(table[1])
    print()
    for row in range(rows):
        for column in range(columns):
            if column < columns - 1:
                print(' ', f'{table[row][column]}', end='  │')
            else:
                print(' ', f'{table[row][column]}', end='')
        print()
        if row < rows - 1:
            print('─────┼─────┼─────')


def playerMove(table: list, XorO: str):                                         # playerMove

    print(f'\nTurn of player {XorO}!')
    row = int(input('> insert row (1, 2, 3): '))
    column = int(input('> insert column (1, 2, 3): '))

    while row > 3 or column > 3:                                                # checks for valid move
        print('\ninvalid move. Try again')                                      # : move out of range
        row = int(input('> insert row (1, 2, 3): '))
        column = int(input('> insert column (1, 2, 3): '))

    while table[row-1][column-1] in 'OX':                                       # checks for valid move
        print('\ninvalid move. Try again')                                      # : if X or O already in place
        row = int(input('> insert row (1, 2, 3): '))
        column = int(input('> insert column (1, 2, 3): '))

    table[row-1][column-1] = XorO                                               # inserts move

main()
