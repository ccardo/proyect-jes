##
#   program that has an out-of-range error
#

def main():

    try:
        myList = [1, 2, 3, 4, 5]
        for i in range(len(myList)+1):
            myList[i] = 'A'

    except IndexError as out_of_range:
        print('Index error:', out_of_range)

main()
