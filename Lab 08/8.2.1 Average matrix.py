##
#   yea

def main():
    from random import randint

    matrix = list()
    rows = int(input("insert rows: "))
    columns = int(input("insert columns: "))
    for _ in range(columns):
        randomRow = [randint(1, 100) for _ in range(rows)]
        matrix.append(randomRow)
    print(*matrix, sep='\n')
    print()

    averaged_matrix = []
    for i, row in enumerate(matrix):
        averaged_row = []
        for j, num in enumerate(row):

            start_i = i-1 if i != 0 else i
            end_i = i+1 if i != len(matrix) else i

            start_j = j-1 if j != 0 else j
            end_j = j+1 if j != len(row) else j

            rowsNums = matrix[start_i:end_i+1]
            to_take_average = []
            for ele in rowsNums:
                to_take_average.append(ele[start_j:end_j+1])

            nums = []
            for ele in to_take_average:
                nums += [ele1 for ele1 in ele]

            averaged_num = round(sum(nums) / len(nums), 2)
            averaged_row.append(averaged_num)
        averaged_matrix.append(averaged_row)

    print(*averaged_matrix, sep='\n')


if __name__ == '__main__':
    main()
