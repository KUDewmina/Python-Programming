def fill_matrix_spiral(values, rows, cols):
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    idx = 0

    while top <= bottom and left <= right and idx < len(values):
        # Left to Right
        for col in range(left, right + 1):
            if idx < len(values):
                matrix[top][col] = values[idx]
                idx += 1
        top += 1

        # Top to Bottom
        for row in range(top, bottom + 1):
            if idx < len(values):
                matrix[row][right] = values[idx]
                idx += 1
        right -= 1

        # Right to Left
        for col in range(right, left - 1, -1):
            if idx < len(values):
                matrix[bottom][col] = values[idx]
                idx += 1
        bottom -= 1

        # Bottom to Top
        for row in range(bottom, top - 1, -1):
            if idx < len(values):
                matrix[row][left] = values[idx]
                idx += 1
        left += 1

    return matrix
