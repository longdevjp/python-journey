# Creating Variables
x = 5
y = "Long"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = "Short"
x = 10
print(x)

# Casting (Ép)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))

# Single or Double Quotes?
x = "John"
# is the same as
x = 'John'

# Case-Sensitive
a = 4
A = "Sally"
# A will not overwrite a
print(A)