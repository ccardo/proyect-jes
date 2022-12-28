##
# generates a list with integers between 0 and 100, removes the smallest value and computes the sum
def sum_without_smallest(integers):
    minimum = 10 ** 6
    for i in integers:
        if i < minimum:
            minimum = i
    return sum(integers) - minimum


def main():
    import random as r
    integers = [r.randint(0, 100) for _ in range(10)]
    print(integers)
    print(f'minimum = {min(integers)}')
    print(f'sum without smallest = {sum_without_smallest(integers)}')

main()
