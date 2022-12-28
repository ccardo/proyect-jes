##
# this program factors out any given integer
# , and prints its prime factors in a list.
import math


def main():
    integer = int(input("> Enter an integer: "))
    factors = ''
    tmp = integer
    x = 2

    while x <= tmp:
        while tmp % x != 0:
            x += 1
            if x > math.sqrt(integer) and factors == '':
                exit(f'\n{integer} is prime.')
        tmp = int(tmp / x)
        factors += f'{x}, '
    factors = factors.removesuffix(', ')
    print(f'\nPrime factors of {integer}:\n{factors}')


if __name__ == '__main__':
    main()
