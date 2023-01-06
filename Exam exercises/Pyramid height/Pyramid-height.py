##
#

def main():

    with open("map.txt", "r") as file:
        mapArray = [list(map(int, line.split())) for line in file]

    tops = list()
    for i, row in enumerate(mapArray):

        for j, height in enumerate(row):

            start_i = i-1 if i != 0 else i
            end_i = i+1 if i != len(mapArray) - 1 else i

            start_j = j-1 if j != 0 else j
            end_j = j+1 if j != len(row) - 1 else j

            surroundings = [row[start_j: end_j + 1] for row in mapArray[start_i: end_i + 1]]

            center = row[j]
            if i == 0:
                surroundings[0].remove(center)
            else:
                surroundings[1].remove(center)

            if is_pyramid(surroundings, center):
                print(f"{center}: ({j}, {i})")
                tops.append(center)

    print(f"average height of the pyramids: {sum(tops) / len(tops)}")


def is_pyramid(array: list[list], center):

    result = set()
    for row in array:
        for height_level in row:
            result.add(height_level)

    if len(result) == 1 and all(i < center for i in result):
        return True
    return False


if __name__ == '__main__':
    main()
