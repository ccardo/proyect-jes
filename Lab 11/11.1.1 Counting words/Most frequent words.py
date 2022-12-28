##
#
import Counting_words as CW

print()
for i in range(5):
    mostUsed = max(CW.glossary, key=CW.glossary.get)
    print(f"{i+1}.{mostUsed.capitalize():<5} -> {CW.glossary.get(mostUsed):>5}")
    del CW.glossary[mostUsed]
