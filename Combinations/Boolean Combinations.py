def generate_combinations(n):  # This function generates all possible binary combinations for n Boolean variables.
    """Generate all binary combinations for n variables"""
    print([format(i, f'0{n}b') for i in range(2 ** n)])

generate_combinations(3)

 # format(i, f'0{n}b') -> This converts number i into a binary string.

# Output -> ['000', '001', '010', '011', '100', '101', '110', '111']
