matrix = []

while True :
    row_input = input()
    if row_input == '-1' :
        break
    else:
        try:
            row = list(map(int, row_input.split()))
            matrix.append(row)
        except:
            print("Error")
            exit()
        if len(row) != len(matrix[0]):
            print("Invalid Matrix")
            exit()

    no_of_rows = len(matrix)
    no_of_columns = len(matrix[0])

# Change the way to creating transposed matrix in better way
transposed_matrix = [[0]*no_of_rows for _ in range(no_of_columns)]

for i in range(no_of_rows):
    for j in range(no_of_columns):
        transposed_matrix[j][i] = matrix[i][j] 
      
for new_row in transposed_matrix:
    for element in new_row:
        print(element,end=" ")
    print()
