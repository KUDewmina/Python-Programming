def spiral_m(matrix):
    left = 0
    right = len(matrix[0])
    top = 0
    bottom = len(matrix)
    spiral_m  = []
    # goes to right to left
    while left< right and top < bottom :
        for i in range(left, right):
            spiral_m.append(matrix[top][i])
        top += 1
        for i in range(top,bottom):
            spiral_m.append(matrix[i][right-1])
        right -= 1
        for i in range(right-1, left-1,-1):
            spiral_m.append(matrix[bottom-1][i])
        bottom -= 1
        for i in range(bottom-1, top-1,-1):
            spiral_m.append(matrix[i][left])
        left += 1
    print(spiral_m)


matrix = [ [1, 2, 3,4],
           [5, 6,7,8],
           [9,10,11,12],
           [13,14,15,16]
           ]


spiral_m(matrix)
