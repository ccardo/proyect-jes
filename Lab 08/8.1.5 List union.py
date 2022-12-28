##
#   function = merge(), joins two lists alternating each one's elements
#

def merge(a: list, b: list):

    shorter = a if len(a) < len(b) else b
    longer = b if shorter == a else a

    for i, n in enumerate(shorter):                      # takes the shortest list
        longer.insert(2*i+1, shorter[i])                 # inserts the elements from the shortest list into the longest

    return longer

A, B = [1, 3, 5, 7, 9, 11, 13, 15], [2, 4, 6, 8, 10, 12, 14, 16]
print(merge(A, B))
