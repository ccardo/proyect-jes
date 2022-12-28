##
# checks whether two number lists have the same elements, no matter the order
def main():
    import random as r
    setA = [r.randint(1, 10) for _ in range(5)]
    setB = [r.randint(1, 10) for _ in range(5)]
    print(f'{setA}\n{setB}')
    print(same_set(setA, setB))


def same_set(a: list, b: list):
    A = sorted(a)
    B = sorted(b)
    if A == B:
        return True
    return False

main()
