##
# generates a random 10-element list, checks if there is any local maximum.
# if so, prints the first that is found
def main():

    # noinspection PyGlobalUndefined
    global localMax
    from random import randint
    integers = [randint(0, 100) for _ in range(10)]
    print(integers, '\n')

    for i, n in enumerate(integers):
        if 0 < i < len(integers) - 1:

            if integers[i-1] < n > integers[i+1]:
                localMax = True
                print(f'found a local maximum at {n}')
                break
            else:
                localMax = False

    if not localMax:
        print(f'There are no local maxima in {integers}')

main()
