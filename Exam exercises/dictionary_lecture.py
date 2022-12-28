##
#   what are dictionaries?

"""
dictionaries:
two-dimensional data structures;

{key: value}

> immutable;
> doesn't allow duplicates;
> unordered;
> searched not by index but rather by KEY

"""

# ways to create an empty dictionary
myDict_0 = {}
myDict_1 = dict(numerouno='germano', numerodos='jacinto')

# traversing a dictionary:
# use for loop
for key in myDict_1:
    print(key, ":", myDict_1.get(key))

"""
iterating dictionaries mroe efficiently:
> use items() method
> returns a list of tuples (key, value)
"""
tapols = myDict_1.items()
for tapol in tapols:
    print(tapol, end='\n')

# can also sort the information in a dictionary:
hermano = sorted(myDict_1)
print(hermano)

"""
EXAMPOL:

> we want to print the index at the end of a book
> how many times are certain words used in certain pages?
> use dickshonarìs
"""

"pòp metod"

