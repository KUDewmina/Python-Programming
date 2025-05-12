def combinations(arr, r, start=0, path=[]):
    if len(path) == r:  # Base case: If path has r elements, print it
        print(path)
        return
    for i in range(start, len(arr)):
        combinations(arr, r, i + 1, path + [arr[i]])  # Recurse with next elements

# Example usage:
combinations([1, 2, 3, 4], 2)
