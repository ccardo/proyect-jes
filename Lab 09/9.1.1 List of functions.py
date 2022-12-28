##
#   list of functions
#   doing different stuff IDK

# I Swap the first and last element of a list;
def swap_first_last(List: list) -> list:
    List[0], List[-1] = List[-1], List[0]
    return List


# II shift every element 1 index to the right, handle wraparound;
def shift_index_right(List: list) -> list:
    last = List[-1]
    List.insert(0, last)
    return List


# III replace alla even elements with 0;
def replace_even_with0(List: list) -> list:

    evenZeros = list(
        map(
            lambda x: 0 if x % 2 == 0 else x,
            List
        )
    )
    return evenZeros


# IV replace each element (besides first and last) by the larger of its two neighbors;
def replace_each_element_besides_first_and_last_by_the_larger_of_its_two_neighbors(List: list) -> list:

    tuples = [(List[i - 1], n, List[i + 1])
              for i, n in enumerate(List)
              if 0 < i < len(List) - 1]

    import itertools as IT
    tuples = list(IT.starmap(max, tuples))
    tuples.insert(0, List[0])
    tuples.append(List[-1])
    return tuples


# V remove the middle element if the list length is odd, or the middle two elements if the list length is even;
def remove_the_middle_element_if_the_list_length_is_odd_or_the_middle_two_elements_if_the_length_is_even(List: list):
    index = (len(List) - 1) // 2
    middle = 1 if len(List) % 2 else 2
    return List[:index] + List[index+middle:]


# VI return the second-largest element of the list;
def return_the_second_largest_element_of_the_list(List: list) -> float:
    List.remove(max(List))
    return max(List)


# VII return True if the list is currently sorted in increasing order;
def return_True_if_the_list_is_currently_sorted_in_increasing_order(List: list) -> bool:
    if List == sorted(List):
        return True
    return False


# VIII return True if the list contains two adjacent duplicate elements;
def return_True_if_the_list_contains_two_adjacent_duplicate_elements(List: list) -> bool:
    import itertools as IT
    couples = IT.pairwise(List)
    dupes = list(filter(lambda x: x[0] == x[1], couples))
    return True if dupes else False


# IX return True if the list contains duplicate elements (which neet not be adjacent);
def return_True_if_the_list_contains_duplicate_elements_which_neet_not_be_adjacent(List: list) -> bool:
    for i in List:
        return True if List.count(i) > 1 else False
