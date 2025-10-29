'''
Operator	Description	                                            Example	
is 	        Returns True if both variables are the same object	    x is y	
is not	    Returns True if both variables are not the same object	x is not y
'''

# is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# is not
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)