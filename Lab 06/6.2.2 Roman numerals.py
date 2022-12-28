##
# this function will convert any roman numeral into an integer
#

def rnToInt(romanNumeral):
    numbers = 'IVXLCDM'
    integer = 0
    previousNumber = 0
    currentNumber = -1

    for index, character in enumerate(romanNumeral):
        findChar = numbers.find(character)

        if findChar % 2 != 0:
            currentNumber = 5 * (10 ** (findChar // 2))
        elif findChar % 2 == 0:
            currentNumber = 10 ** (findChar // 2)

        if previousNumber < currentNumber <= 10 * previousNumber:
            integer = integer - (2 * previousNumber)
        elif previousNumber < currentNumber and currentNumber > 10 * previousNumber and index > 0:
            print('Type your roman numeral correctly.')
            return
        previousNumber = currentNumber

        integer += currentNumber
    return integer

if __name__ == '__main__':
    print(rnToInt(input('Enter a valid roman numeral: ')))
