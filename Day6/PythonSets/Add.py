# Add Set Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) # Output: {'banana', 'cherry', 'apple', 'papaya', 'mango', 'pineapple'}

# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

