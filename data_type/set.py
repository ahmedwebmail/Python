# Can't put duplicate values in a set. The set will automatically remove duplicates.
# And sets are unordered, meaning that the items have no index.

# Normal set
normal_set = {1, 2, 3, 4, 5}
print("Normal Set:", normal_set)

# Frozen set - immutable set, cannot be changed after creation
frozen_set = frozenset([1, 2, 3, 4, 5])
print("Frozen Set:", frozen_set)