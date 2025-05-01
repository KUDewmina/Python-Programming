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

transposed_matrix = []
    

for i in range(no_of_columns):
    new_row = []
    for j in range(no_of_rows):
        new_row.append(matrix[j][i]) 
    transposed_matrix.append(new_row)
for new_row in transposed_matrix:
    for element in new_row:
        print(element,end=" ")
    print()
