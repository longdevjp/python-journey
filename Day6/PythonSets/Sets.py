# Python Sets
myset = {"apple", "banana", "cherry"}
# Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # Output: {'banana', 'cherry', 'apple'}

# The values True and 1 are considered the same
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) # Output: {1, 2, 'banana', 'cherry', 'apple'}

# The values False and 0 are considered the same value in sets
thisset = {"apple", "banana", "cherry", False, 0, 2}
print(thisset) # Output: {0, 2, 'banana', 'cherry', 'apple'}

# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
print(set1)
print(set2)
print(set3)
print(set4)

# <class 'set'>
myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

