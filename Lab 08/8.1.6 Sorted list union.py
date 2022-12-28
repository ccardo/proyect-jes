##
#   function = merge_sorted(), alternates between element of each list, returns an ordered list
#   without using the sort() method and sorted() function

def merge_sorted(a, b):

    shorter = a if len(a) < len(b) else b
    longer = b if shorter == a else a
    # merging lists
    for i, n in enumerate(shorter):
        longer.insert(2*i+1, shorter[i])

    # sorting big list without using sorting builtins (bullshit)
    sortedList = []
    list1 = longer[::-1][::-1]
    for _ in longer:
        highest = max(list1)
        list1.remove(highest)
        sortedList.append(highest)

A, B = [7, 7, 7, 7], [3, 3, 3, 3]
print(merge_sorted(A, B))
