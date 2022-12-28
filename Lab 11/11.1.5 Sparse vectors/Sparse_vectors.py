##
#

def create_sparse_vector():
    import random as rd
    vector_dict = {}
    sparse_vector = [rd.randint(0, 10) for i in range(rd.randint(1, 15))]
    for i, value in enumerate(sparse_vector):
        if value != 0:
            vector_dict.update({i: value})

    return vector_dict


def sum_sparse_vectors(vec1: dict, vec2: dict):

    total = {}
    longer = max([vec1, vec2], key=len)
    shorter = vec1 if longer == vec2 else vec2
    for j in shorter:
        if j not in longer:
            total.update({j: shorter[j]})
    for i in longer:
        total.update({i: longer[i]})
        if i in shorter:
            total.update({i: longer[i] + shorter[i]})

    return total


if __name__ == '__main__':

    vector_1 = create_sparse_vector()
    vector_2 = create_sparse_vector()
    sum_vector = sum_sparse_vectors(vector_1, vector_2)
    print(vector_1, vector_2, f"Sum of sparse vectors:\n{sum_vector}", sep='\n')
    sum_vector_list = [0] * (max(sum_vector)+1)
    for position in sum_vector:
        sum_vector_list[int(position)] = sum_vector[position]
    print("Sum vector in sparse representation:")
    print(*sum_vector_list, sep="  ")
