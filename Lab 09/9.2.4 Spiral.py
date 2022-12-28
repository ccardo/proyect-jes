##
#   print a table in a spiral manner with numbers

def main() -> None:

    SideLength = int(input("enter side length for the table: "))
    matrix = [[0]*SideLength for _ in range(SideLength)]

    start = 1
    for ring in range(SideLength//2):
        start = build_ring(matrix, ring, start)

    if SideLength % 2 == 1:
        matrix[SideLength//2][SideLength//2] = start

    for row in matrix:
        for col in row:
            print(f"{col:^3}", end=" ")
        print()


def build_ring(matrix, ring, start):

    side_length = len(matrix)

    # go right
    for col in range(ring, side_length - ring):
        matrix[ring][col] = start
        start += 1

    # go down to the end of the ring
    for row in range(ring + 1, side_length - ring):
        matrix[row][side_length - ring - 1] = start
        start += 1

    # go to the left to fill the bottom of the ring with numbers
    for col in range(side_length - ring - 2, ring - 1, -1):
        matrix[side_length - ring - 1][col] = start
        start += 1

    # go upwards until the end of the ring
    for row in range(side_length - ring - 2, ring, -1):
        matrix[row][ring] = start
        start += 1

    return start

main()
