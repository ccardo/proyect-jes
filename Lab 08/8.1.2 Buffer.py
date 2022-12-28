##
#   buffer program: shifts every element up 1 index
#   except for the last one, which wraps around to the first index

def main():

    userInput = input('> Type a word... ')

    myList = [*userInput]

    print(*myList, sep=', ')

    last = myList.pop()
    myList.insert(0, last)

    print(*myList, sep=', ')

main()
