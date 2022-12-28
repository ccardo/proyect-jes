##
# this function counts the words in a string
#

def countWords(string):
    wordCount = 1
    for index, character in enumerate(string):
        if character == ' ' and character is not string[index + 1]:
            wordCount += 1
    return wordCount

if __name__ == '__main__':
    print(f'> words in the string: {countWords(input("Get string: "))}')
