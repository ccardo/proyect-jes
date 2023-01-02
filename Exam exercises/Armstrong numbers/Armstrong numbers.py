##
#

def main():

    # usual thing with the file error handling
    try:
        with open("numbers.txt", "r") as file:
            numbers = list(map(str.strip, file.readlines()))
    except IOError:
        exit("The file does not exist, or the file name was typed incorrectly.")

    # list comprehension like you've never seen before
    with open("armstrong.txt", "w") as output:
        [output.write(f"{num}\n") for num in numbers if armstrong_number(num)]


def armstrong_number(number: str) -> bool:

    """checks if the number equals the sum of each
    of its digits raised to the len(number) power."""

    n = len(str(number))
    total = [int(i) ** n for i in number]
    return sum(total) == int(number)


if __name__ == '__main__':
    main()
