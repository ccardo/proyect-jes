##
# this program removes the minimum value from a list
# without using the min() or the remove() functions
def main() -> None:
    import random as r
    Integers = [r.randint(0, 100) for _ in range(10)]
    print(f'number list: {Integers}')
    print(f'list without smallest value: {remove_min(Integers)}')
    return


def remove_min(LIST: list):
    smallest = LIST[0]
    smallestIndex = 0
    for i, n in enumerate(LIST):
        if i > 0 and n < smallest:
            smallest = n
            smallestIndex = i
    LIST.pop(smallestIndex)
    return LIST

main()
