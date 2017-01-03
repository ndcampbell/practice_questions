#Zero Matrix: If an element in MxN matrix is 0, entire row and column are set to 0

def zero_matrix(matrix):
    zero_i = None
    rows = []
    cols = []
    for i, row in enumerate(matrix):
        if 0 in row:
            rows.append(i)
            cols.append(row.index(0))

    if len(rows) == 0:
        return matrix

    for i, row in enumerate(matrix):
        if i in rows:
            matrix[i] = [0]*len(row)
        else:
            for col in cols:
                matrix[i][col] = 0

    return matrix

if __name__ == "__main__":
    example = [ [1,2,3,4],
                [1,2,0,4],
                [1,0,3,4],
                [1,2,3,4]]

    print(zero_matrix(example))
