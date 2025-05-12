import itertools

items = ['A', 'B', 'C']

# All combinations of length 2
comb = list(itertools.combinations(items, 2))
print("Combinations:", comb)
