##
# these functions return the diameter of a wire,
# and the resistance of an aluminum wire and copper wire
# based on the gauge and length
def main():
    L = float(input('> length of wire = '))
    G = int(input('> Gauge of wire [int] = '))
    M = input('> Material of wire [copper, aluminum] = ')
    print(f'\nThe diameter of the wire, in mm: {diameter_mm(G)}')
    print(f'The resistance of the wire is: {wireRes(L, G, M)}')


def diameter_mm(gauge):
    return 0.127 * 92 ** ((36 - gauge) / 39)


def wireRes(length, gauge, material='copper'):
    # noinspection PyGlobalUndefined
    global Resistivity
    if material.lower() == 'copper':
        Resistivity = 1.678 * (10 ** -8)  # Ohm * m
    elif material.lower() == 'aluminum':
        Resistivity = 2.82 * (10 ** -8)  # Ohm * m
    diameter = diameter_mm(gauge)
    Resistance = 4 * Resistivity * length / (3.141592 * (diameter ** 2))

    return Resistance

if __name__ == '__main__':
    main()
