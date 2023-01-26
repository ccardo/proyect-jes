#

def create_canvas():
    return [["."] * 20 for i in range(20)]


def main():

    canvas = create_canvas()

    with open("commands.txt") as file_input:
        commands = [line.split() for line in file_input]
    
    commands_chars = {
        "P": "*",
        "V": "|",
        "H": "-"
    }

    for command in commands:

        char, col, row = command[0], int(command[1]), int(command[2])
        length = int(command[3]) if len(command) > 3 else 1

        dist_x, dist_y = 0, 0

        for _ in range(length):
            
            canvas[row + dist_y][col + dist_x] = commands_chars[char]

            if char == "V":
                dist_y += 1
            elif char == "H":
                dist_x += 1
    
    chars = ["|", "-"]
    for i, row in enumerate(canvas):
        
        if i == 0:
            previous_row = row
        if i == len(canvas) - 1:
            next_row = row
        previous_row, next_row = canvas[i-1], canvas[i+2]

        for j, col in enumerate(row):

            if j == 0:
                previous_col = col
            if j == len(row) - 1:
                next_col = col
            
            if char in chars and (
                
            )
        

    for row in range(20):
        for col in range(20):
            print(canvas[row][col], end=" ")
        print()


if __name__ == "__main__":
    main()