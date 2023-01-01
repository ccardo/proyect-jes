##
#

def main():
    coords, size = None, None

    # lets user input correct values for the coordinates and the size of the square
    while not coords and not size:
        coords_input = input("input the desired coordinates (x,y):\n").split(",")
        size_input = input("input the size of the square to analyze:\n")
        try:
            coords = list(map(int, coords_input))
            size = int(size_input)
        except ValueError:
            print("\ncoords or size were of incorrect value. Try again:")

    # open the file and read the sequence
    try:
        with open("landscape.txt", "r") as infile:
            lines = infile.readlines()
            total_size = len(lines), len(lines[0])

            # checks if the coordinates are valid (x <= 401, y <= 76)
            if coords[0] + size <= total_size[1] and coords[1] + size <= total_size[0]:
                analyzed = [row[coords[0]: coords[0] + size] for row in lines[coords[1]: coords[1] + size]]
            else:
                exit("Size too big to fit into the picture.")

            # creates a dictionary with every character and its usage count
            characters = dict()
            for line in analyzed:
                for char in line:
                    if char not in characters:
                        characters.update({char: 1})
                    else:
                        characters[char] += 1

            for char in characters:
                print(f"{char!r} --> {round((characters[char] / size ** 2) * 100, 3)}%")

    except IOError:
        exit("No file was found. ")


if __name__ == '__main__':
    main()
