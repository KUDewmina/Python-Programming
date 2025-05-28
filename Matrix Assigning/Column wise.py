string= "HELLOTHERE"
n = 3
rows = 3
if len(string)%n != 0:
   columns = n+1
else:
   columns = n

matrix = [[0]*columns for _ in range(rows)]

k=0
for i in range(columns):
   for j in range(rows):
      if k<len(string):
         matrix[j][i]=string[k]
         k+=1

for i in range(rows):
   for j in range(columns):
      if matrix[i][j]==0:
         matrix[i][j]="*"

for row in matrix:
   print(' '.join(row))  
  
# Output
''' 
    H L H E
    E O E *
    L T R * 
            '''
