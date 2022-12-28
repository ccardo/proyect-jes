##
# this program creates a list of all the prime numbers
# in a set range, given the top and bottom values
from Resources.definitions import isprime

bottomNumber = int(input("Enter bottom number: "))
topNumber = int(input("Enter top number: "))

while bottomNumber <= topNumber:
    # the imported function is in my Resources folder under pythonProject
    if isprime(bottomNumber):
        print(f'The prime numbers between {bottomNumber} and {topNumber} are:')
        print(f'{bottomNumber}', end=', ')
    bottomNumber += 1
