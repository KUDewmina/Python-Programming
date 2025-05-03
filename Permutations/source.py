def permutations(arr, path=[]):
  if not arr:
    print(tuple(path)) # Base case -> if the array is empty,print the current permutatation
    return # Backtracking

  for i in range(len(arr)):
    permutations(arr[:i]+arr[i+1:] ,path+[arr[i]])

arr = input().split()
permutations(arr)
