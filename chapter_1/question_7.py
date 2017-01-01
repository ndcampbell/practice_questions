#rotate matix: given an image represented by NxN matrix, each pixel is 4 bytes, rotate the image by 90 degrees. Can it be done in place?

# example:
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
#
# Output:
# 1 1 1 1
# 2 2 2 2
#
#
#

#Python doesnt specifically have matrices. Using a nested list. Can use numpy for matrix if more complicated logic is necessary
def rotate_matrix(matrix):
    width = len(matrix)
    new_matrix = []
    for i in range(width):
        new_matrix.append([0]*width)
        for j in range(width):
            new_matrix[i][-j] = matrix[i][i]
    return new_matrix

def print_matrix(matrix):
    for row in matrix:
        print(str(row))


if __name__ == "__main__":
    example = [ [1,2,3,4],
                [1,2,3,4],
                [1,2,3,4],
                [1,2,3,4]]
    rotate_matrix(example)
