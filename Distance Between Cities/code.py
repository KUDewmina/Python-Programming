n = int(input()) # Number of cities
distances = list(map(int, input().split())) 
# Compute comulative distances from city 1 to each city
comulative_distances = []
for i in range(n):
    sum=0
    for j in range(i):
        sum+=distances[j]
    comulative_distances.append(sum)

matrix=[[0]*n for _ in range(n)]
# Fill the distance matrix
for i in range(n):
    for j in range(n):
        matrix[i][j]=abs(comulative_distances[j]-comulative_distances[i])
print(matrix)
