##


def main():

    try:
        with open("landscape_1.txt") as file:
            landscape = [i.strip("\n") for i in file]
    except IOError as e:
        exit(e)

    row, col, size = input_frame(landscape)

    frame = [char for landscape_row in landscape[row: row + size] for char in landscape_row[col: col + size]]
    chars = {character: 0 for character in frame}

    for char in chars:
        chars[char] += frame.count(char)

    most_present_characters = sorted(chars, key=chars.get, reverse=True)
    for character in most_present_characters:
        percentage = chars[character] / sum(chars.values()) * 100
        print(f'"{character}"{round(percentage, 3):>10}%')


def input_frame(landscape):
    try:
        user_input_coords = input("Insert the top-left corner coordinates (X, Y) of the frame, separated by a space: ")
        col, row = map(int, user_input_coords.split())
        side_length = int(input("Insert the side length of the frame: "))

        if side_length + col >= len(landscape[0]) or side_length + row >= len(landscape): raise IndexError
        if side_length == 0: raise ValueError("side length cannot be zero.")
        return row, col, side_length

    except ValueError as e:
        exit(f"Error: {e}")
    except IndexError:
        exit("Error: frame too large to fit in the landscape.")

if __name__ == '__main__':
    main()