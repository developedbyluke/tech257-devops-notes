frozen_set = frozenset(["hello", "world"])

# Cannot add "!" to frozen_set as a frozen set is immutable meaning their elements cannot be changed after creation.

normal_set = {"let's", "learn"}

normal_set.add(frozen_set)

print(normal_set)

# Adding the frozen set to the normal set worked because frozen sets are immutable. They can be used as dictionary keys too.

# After running this script half a dozen times, it is noticeable that the order of the items in the set can appear in any order. This is because sets are unordered.

# Frozen sets are different to normal sets because they are immutable. This means their elements cannot be changed after creation and nothing can be added or removed to them.
