##
a = float(input('insert a number: '))
b = float(input('insert a number: '))
c = float(input('insert a number: '))

if a > b > c:
    print('the function is strictly DECREASING')
elif c > b > a:
    print('the function is strictly INCREASING')
else:
    print('neither')
