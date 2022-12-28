##
#

def create_number_list() -> set:

    upper = int(input("Insert the top number: "))
    set_ = {i for _ in range(2, upper)}
    return set_


def remove_multiples_of(n, numbers: set) -> set:

    return set(filter(lambda x: x % n != 0, numbers))


if __name__ == '__main__':
    from math import sqrt

    integers = create_number_list()

    for i in range(2, round(sqrt(max(integers)))):
        integers = remove_multiples_of(i, integers)
    print(integers)
