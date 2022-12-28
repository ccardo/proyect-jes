##
from math import sqrt

n1 = 1
n2 = 1
if n1 == n2:
    print(n1, 'is equal to', n2)
else:
    print(n1, 'is not equal to', n2)
n1 = 1
n2 = 1.0
if n1 == n2:
    print(n1, 'is equal to', n2)
else:
    print(n1, 'is not equal to', n2)
n1 = 2.0
n2 = sqrt(4)
if n1 == n2:
    print(n1, 'is equal to', n2)
else:
    print(n1, 'is not equal to', n2)
n1 = '1'
n2 = 1
if n1 == n2:
    print(n1, 'is equal to', n2)
else:
    print(n1, 'is not equal to', n2)
n1 = 'Hello'
n2 = 'hello'
if n1 == n2:
    print(n1, 'is equal to', n2)
else:
    print(n1, 'is not equal to', n2)
