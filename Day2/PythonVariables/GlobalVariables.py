# Global Variables
name = "Long"
def myfunc():
    print("Hello " + name)
myfunc()

x = "DoLong"
def myfunc2():
    x = "Hello"
    print(x)
myfunc2()
print(x)

# The global Keyword
def myfunc3():
    global y
    y = "Hello"
myfunc3()
print("test3 = ", y)

"""To change the value of a global variable inside a function, 
refer to the variable by using the global keyword:"""
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)