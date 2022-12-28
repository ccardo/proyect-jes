##
#  generates a random 20-element list, prints it and then prints it in a sorted order
def main():
    import random as r
    integers = [r.randint(0, 99) for _ in range(20)]
    print(integers)
    integers.sort()
    print(integers)

main()
