##
LongSequence = str(input('insert a DNA sequence: '))
ShortSequence = str(input('insert a 3-character DNA sequence: '))
if 'A' and 'T' and 'C' and 'G' in LongSequence and len(LongSequence) == 20 and len(ShortSequence) == 3:
    if ShortSequence in LongSequence:
        print('the short sequence appears in the long sequence at:', LongSequence.find(ShortSequence))
        print('the short sequence appears in the long sequence', LongSequence.count(ShortSequence), 'times')
    else:
        exit('fai cacare')
