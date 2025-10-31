# Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) # Output: ('apple', 'kiwi', 'cherry')

# Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) # Output: ('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) # Output: ('apple', 'banana', 'cherry', 'orange')

# Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)
print(thistuple) # Output: ('apple', 'cherry')

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

