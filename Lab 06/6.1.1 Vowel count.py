##
# this function counts the vowels present in a string
#

def countVowels(string):
    count = 0
    for char in string:
        if char.lower() in 'aeiou':
            count += 1
    return count

if __name__ == '__main__':
    print(f'n. of vowels in string: {countVowels(input("Get string: "))}')
