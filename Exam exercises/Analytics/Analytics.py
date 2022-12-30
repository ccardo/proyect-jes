##
#   analytics.txt related code

with open("analytics.txt", "r") as germano:
    lines = germano.readlines()                              # create a list with every element of analytics.txt in the
    lines = list(line.strip().split(":") for line in lines)  # form of a list: ['word', 'page'] using the split() method
    glossary = {}                                            # glossary will contain {"word": {every page it's used in}}
    #
    for text in lines:
        pages = set()
        text.reverse()                          # (step not necessary, used to make it more intuitive)
        if text[0] not in glossary:             # update "glossary" with the word ONLY if the word isn't already in it;
            glossary.update({text[0]: pages})   # ; if not, the set of pages will be empty each time it's updated
        glossary[text[0]].add(int(text[1]))     # adds the current page to the set regardless of if the word is already
        #                                       # present in "glossary"
    print("\n%-15s%25s\n" % ("WORDS", "PAGES"))
    for key in glossary:
        print("%-15s%25s" % (key, glossary.get(key)))
