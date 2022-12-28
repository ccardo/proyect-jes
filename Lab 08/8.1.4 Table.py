##
#   prints a table with all 0's,
#   then converts it into 1's,
#   then converts it int a checkerboard pattern of 0's and 1's
#   with the top and bottom row of only 1's

def main():
    Rs = int(input('> insert rows: '))
    Cs = int(input('> insert columns: '))
    # create a table of 'Rs' rows and 'Cs' columns
    table = [[0] * Cs] * Rs
    print_table(table, Cs)
    print()

    # fill the cells with 1's
    for i in table:
        for j in range(Cs):
            i[j] = 1
    print_table(table, Cs)
    print()

    # fill table in a checkerboard pattern with 1's and 0's
    for i, row in enumerate(table):
        subRow = row[::-1][::-1]
        for j, num in enumerate(row):
            if i % 2 == 0 and j % 2 == 0:
                subRow[j] = 0
            if i % 2 == 1 and j % 2 == 1:
                subRow[j] = 0
        table[i] = subRow
    print_table(table, Cs)
    print()

    # fill the first and last row with 1's
    table[0] = [1 for _ in range(Cs)]
    table[-1] = table[0]
    print_table(table, Cs)


def print_table(table, columns):
    for i in table:
        for j in range(columns):
            print(i[j], end='  ')
        print()


main()
