##
x = int(input('insert a number: '))
if 0 < x < 100:
    print('x > 0 and x < 100, True')
else:
    print('x > 0 and x < 100, False')

if x > 0 or x < 100:
    print('x > 0 or x < 100, True')
else:
    print('x > 0 or x < 100, False')

if x > 0 or 100 < x:
    print('x > 0 or 100 < x, True')
else:
    print('x > 0 or 100 < x, False')

if 0 < x < 100 or x == -1:
    print('x > 0 and x < 100 or x == -1, True')
else:
    print('x > 0 and x < 100 or x == -1, False')
