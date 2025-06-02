def fill_matrix_column_wise(values, rows):
    cols = (len(values) + rows - 1) // rows  # Calculate number of columns needed
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    for idx, val in enumerate(values):
        col = idx // rows
        row = idx % rows
        matrix[row][col] = val

    return matrix

# Example usage:
values = ['a', 'b', 'c', 'd', 'e', 'f']
rows = 2
matrix = fill_matrix_column_wise(values, rows)

# Print nicely
for row in matrix:
    print(' '.join(row))
