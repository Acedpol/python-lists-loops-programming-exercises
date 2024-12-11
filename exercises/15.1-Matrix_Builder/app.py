# Your code here
def matrix_builder(num):
    rows = []
    for i in range(num):
        cols = []
        for j in range(num):
            cols.append(1)
        rows.append(cols)
    return rows

print(matrix_builder(5))
        