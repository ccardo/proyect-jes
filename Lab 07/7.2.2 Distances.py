##
# drivers tend to maximize the space between each parked car
# this program (hopefully) displays the parking slots being occupied by cars
# procedurally
def main():
    NumberOfSlots = int(input('> n. of parking slots = '))
    SLOTS = ['_' for _ in range(NumberOfSlots)]
    steps = 1

    while steps <= NumberOfSlots:  # registers the index of any "X"
        indicesOfXs = []  # or the index of the initial and final
        for i, c in enumerate(SLOTS):  # position of the slots into a list
            if i == 0 or i == len(SLOTS) - 1:
                indicesOfXs.append(i)
            elif c == "X":
                indicesOfXs.append(i)

        couples = []  # generates a list with every couple
        for i, n in enumerate(indicesOfXs):  # of indices of X's;
            if i > 0:  # the list is composed of tuples
                previous = indicesOfXs[i - 1]  # that contain:
                distance = n - previous  # [0] the distance (diff. of indices)
                couple = distance, previous, n  # [1] the smaller index
                couples.append(couple)  # [2] the greater index
        farthestCouple = max(couples)
        distance, X1, X2 = farthestCouple[0], farthestCouple[1], farthestCouple[2]

        sequence = SLOTS[X1: X2 + 1]  # 'sequence' = longest vacant space
        for i, slot in enumerate(sequence):  # modifies only 'sequence' by adding 1 "X"
            if (i == 0 or i == len(sequence) - 1) and slot != "X" \
                    or (i == distance // 2 and sequence[-1] == "X") and slot != "X":
                sequence[i] = "X"  # then 'sequence' replaces the
                break  # corresponding sequence in 'SLOTS'
        SLOTS[X1: X2 + 1] = sequence

        print(f'\n{steps:>3}.', end='  ')  # prints the parking slots
        for slot in SLOTS:  # after printing the n.of steps
            print(slot, end=' ')
        steps += 1


main()
