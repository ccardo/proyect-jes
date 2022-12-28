##
stringInput = input('Insert any string: ')
digitCount = 0
uppercase = ''
evenPos = ''
vowelString = ''
replacedVowels = stringInput

for index, char in enumerate(stringInput):

    # I = output uppercase
    if char.isupper():
        uppercase = uppercase + char

    # II = output even index letters
    if index % 2 != 0:
        evenPos = f'{evenPos} {stringInput[index]}'

    # III = output same string with vowels replaced by underscore
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for char in replacedVowels:
    if char in vowels:
        replacedVowels = replacedVowels.replace(char, '_')
for index, char in enumerate(stringInput):

    # IV = how many digits are contained in string
    if char.isdigit():
        digitCount += 1

    # V = the position of the vowels
    if char in vowels:
        vowelString = vowelString + char + f'{index + 1}, '

print(f'Uppercase letters: {uppercase}')
print(f'Even position letters: {evenPos}')
print(f'String with replaced vowels: {replacedVowels}')
print(f'Digit count: {digitCount}')
print(f'Position of the vowels: {vowelString}')
