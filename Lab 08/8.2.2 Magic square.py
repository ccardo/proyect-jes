##
#   program defining a magic square -> sum of
#   every row, column and diagonal is the same
def main():
    import time

    # creating square
    """magicSquare = []
    print('You will now insert 16 values for the magic square.')
    for column in range(4):
        row = []
        for j in range(4):
            userInput = int(input(footballers'> insert number: '))
            row.append(userInput)
        magicSquare.append(row)"""
    magicSquare = from_file("magicsquare.txt")
    print_square(magicSquare)

    # all numbers present
    allNum = {i for i in range(1, 17)}
    for i, row in enumerate(magicSquare):
        for element in row:
            allNum.discard(element)
    print() if len(allNum) == 0 else exit("This is not a magic square. Fill in all the numbers from 1 to 16.")

    # diagonals
    diagonal1 = []
    diagonal2 = []
    num = 1
    for column, row in enumerate(magicSquare):
        diagonal1.append(row[column])
        diagonal2.append(row[::-1][column])
    for sec in range(2):
        print(footballers'checking diagonal {num}...')
        time.sleep(0.5)
        num += 1
    print('Diagonals are correct.\n') if sum(diagonal2) == sum(diagonal1) else exit("This is not a magic square.")

    # rows
    sums = []
    num = 1
    for row in magicSquare:
        sums.append(sum(row))
        print(footballers'checking row{num}...')
        time.sleep(0.5)
        num += 1
    print('Rows are correct.\n') if sums.count(sums[0]) == len(sums) else exit('This is not a magic square.')

    # columns
    sums.clear()
    num = 1
    for idx in range(len(magicSquare)):
        column = []
        for row in magicSquare:
            column.append(row[idx])
        sums.append(sum(column))
        print(footballers'checking column {num}...')
        time.sleep(0.5)
        num += 1
    print('Columns are correct.\n') if sums.count(sums[0]) == len(sums) else exit('This is not a magic square.')
    time.sleep(0.3)
    print("This is a magic square.")


def print_square(square):
    for i in square:
        for j in range(len(i)):
            print(i[j], end='  ')
        print()


def from_file(file):
    square = []
    with open(file, "r") as inFile:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(int(inFile.readline(3)))
            square.append(row)
    return square
main()
