##
#
def main():
    import random
    sequence = [random.randint(1, 100) for _ in range(10)]
    print(sequence)
    localMaxima = []
    for idx, num in enumerate(sequence):
        if 0 < idx < len(sequence) - 1:
            if sequence[idx-1] < num > sequence[idx+1]:
                localMax = idx
                localMaxima.append(localMax)

    localMaxima.sort()
    print(f'indices of local maxima: {localMaxima}')
    differences = []
    for idx, num in enumerate(localMaxima):
        if idx > 0:
            previous = localMaxima[idx-1]
            difference = num - previous
            indices = (difference, num, previous)
            differences.append(indices)

    closest = min(differences)
    print(f'closest local maxima (indices): {closest[2]}, {closest[1]}')

main()
