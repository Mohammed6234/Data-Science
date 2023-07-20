set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Using frozenset on set1
frozen_set1 = frozenset(set1)

# Finding elements in set1 that are not in set2
difference_set = set1.difference(set2)
print("Difference between set1 and set2:", difference_set)
