##
# generates a random list of integers, computes the alternating sum of them (- for odd indexes, + for even)
def main():
    from random import randint
    total = [randint(0, 100) for _ in range(randint(5, 20))]
    print(f'starting list: {total}')
    print(f'\n{display_alternating_sum(total)} = {alternating_sum(total)}')


def display_alternating_sum(integers: list):  # returns a string of the alternating sum
    display = ''
    for i, n in enumerate(integers):
        if i == 0:
            display += f'{n}'
            continue
        display += f' - {n}' if i % 2 != 0 else f' + {n}'
    return display


def alternating_sum(integers: list):  # returns the actual value of the alternating sum
    for i, n in enumerate(integers):
        if i % 2 == 1:
            integers[i] = -1 * n
    return sum(integers)

main()
