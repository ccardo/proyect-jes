##
# generates a random 12-element list, then prints out:
# even index values;
# equal values (if any);
# the list in the opposite order;
# the first and last element of the list.

def main():
    import random as r
    randomIntegers = []
    maxLen = 10
    for i in range(maxLen):
        randomIntegers.append(r.randint(1, 100))

    evenIndex = [i for i in randomIntegers if i % 2 == 0]
    equalValue = [i for i in randomIntegers if randomIntegers.count(i) > 1]

    print(f'Even-index values: {evenIndex}')
    print(f'Equal values (if any): {equalValue}')
    print(f'List in reverse order: {randomIntegers[::-1]}')
    print(f'first and last element: {randomIntegers[0]}, {randomIntegers[-1]}')

main()
