import itertools

items = ['A', 'B', 'C']

# All permutations of length 2
perm = list(itertools.permutations(items, 2))
print("Permutations:", perm)
