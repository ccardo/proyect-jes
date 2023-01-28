#
#

def main():

    with open("laser_map.txt") as file:
        lines = map(str.split, file)
        laser_map = [list(map(int, line)) for line in lines]

    for y, _ in enumerate(laser_map):
        for x, _ in enumerate(laser_map[y]):
            if laser_map[y][x] == "-":
                continue
            if is_top(y, x, laser_map):
                start_row, end_row, start_col, end_col = is_top(y, x, laser_map)
                for i, row in enumerate(laser_map[start_row: end_row + 1]):
                    for j, _ in enumerate(row[start_col: end_col + 1]):
                        if i + start_row == y and j + start_col == x:
                            continue
                        laser_map[i + start_row][j + start_col] = "-"
    print(*laser_map, sep="\n")
            


def is_top(row, col, array):

    radius = 1
    done = False
    center = array[row][col]
    top = False
    while not done:

        start_row = row - radius
        if row - radius < 0: start_row = 0

        end_row = row + radius
        if row + radius >= len(array): end_row = len(array) - 1

        start_col = col - radius
        if col - radius < 0: start_col = 0

        end_col = col + radius
        if col + radius >= len(array[0]): end_col = len(array[0]) - 1

        surroundings = [row[start_col:end_col + 1] for row in array[start_row:end_row + 1]]

        count = 0
        if not top:
            for surr_row in array[start_row: end_row+1]:
                count += len([i for i in surr_row[start_col: end_col+1] if i != "-" and i >= center])
                if count >= 2: return False
        top = True

        count = 0
        for surr_row in surroundings:
            if any(i != "-" and i >= center for i in surr_row):
                count += 1
        if count >= 2:
            return start_row, end_row, start_col, end_col

        radius += 1


if __name__ == "__main__":
    main()