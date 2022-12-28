##
# this function will convert any roman numeral into an integer
#

def romanToArab(romanNumeral):
    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    checkRomanNumeral(romanNumeral)
    total = 0
    for index, char in enumerate(romanNumeral):
        for key in dictionary:
            if char == key:
                total = total + dictionary[key]
                break
        previous = dictionary[romanNumeral[index - 1]]
        if index > 0:
            if dictionary[char] > previous:
                total = total - 2 * previous
    return total


# noinspection SpellCheckingInspection
def checkRomanNumeral(romanNumeral):
    forbiddenCombinations = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD']
    for i in forbiddenCombinations:
        if i in romanNumeral:
            exit('Enter a VALID roman numeral. Rerun the code.')


if __name__ == '__main__':
    numeral = input('> Insert valid roman numeral ')
    print(f'{numeral} = {romanToArab(numeral)}')
