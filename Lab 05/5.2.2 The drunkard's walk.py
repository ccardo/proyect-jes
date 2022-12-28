from random import randint
##
# This program calculates the total distance from the origin
# of a drunkard choosing randomly 100 times between 4 directions in a crossroads


def main():
    global turns
    x = 0
    y = 0

    for turns in range(100):
        Direction = randint(1, 4)
        if Direction == 1:
            x += 1
        elif Direction == 2:
            x -= 1
        if Direction == 3:
            y += 1
        elif Direction == 4:
            y -= 1
    print(f'The drunkard has crossed {turns + 1} crossroads and is left at: ({x}, {y}) position.')

if __name__ == '__main__':
    main()
