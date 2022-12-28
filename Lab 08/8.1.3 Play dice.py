##
#   generate 20 random dice rolls (1, 6)
# print the longest sequence of equal rolls in brackets

def main():
    import random

    random_20_rolls = [random.randint(1, 6) for _ in range(20)]
    diceRolls = ""
    for roll in random_20_rolls:
        diceRolls += str(roll)

    longest = longest_sequence(diceRolls)
    startingIndex = diceRolls.find(longest)
    endingIndex = startingIndex + len(longest)

    newDiceRolls = f"{diceRolls[:startingIndex]}({longest}){diceRolls[endingIndex:]}"
    print(newDiceRolls)


def longest_sequence(numbers) -> str:

    from itertools import groupby
    sequence = max([list(group) for _, group in groupby(numbers)], key=len)

    sequenceString = ""
    for i in sequence:
        sequenceString += i

    return sequenceString

if __name__ == '__main__':
    main()