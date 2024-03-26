# Sets differ from lists and tuples as you change a

fruits = {"apple", "banana", "cherry"}

print(fruits)

fruits.add("orange")

print(fruits)

fruits.remove("banana")

print(fruits)

fruits.add("apple")

print(fruits)

# Observation: the new item "apple" wasn't added to the set.
# Why: Sets ignore duplicate values

# Problem printing the 2nd item in the set: You cannot access items in a set by referring to an index or key because sets are unordered
# Workaround

print(list(fruits)[1])
