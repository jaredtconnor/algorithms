"""" 
    Hi, here's your problem today. This problem was recently asked by Twitter:

    Given a matrix, transpose it. Transposing a matrix means the rows are now the column and vice-versa.

    Here's an example:
    def transpose(mat):
      # Fill this in.

    mat = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    print(transpose(mat))
    # [[1, 4],
    #  [2, 5],

"""


def transpose(matrix):

    if matrix is None or len(matrix) == 0:
        return []

    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


def print_matrix(matrix):
    for row in matrix:
        print(f"{row}")
       


mat = [[1, 2, 3], [4, 5, 6]]

print_matrix(transpose(mat))
