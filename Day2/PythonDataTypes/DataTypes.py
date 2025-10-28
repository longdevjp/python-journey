"""
Kiểu văn bản:	str
Các kiểu số:	int, float, complex
Các loại trình tự:	list, tuple, range
Loại bản đồ:	dict
Các loại tập hợp:	set,frozenset
Kiểu Boolean:	bool
Các loại nhị phân:	bytes, bytearray, memoryview
Không có Loại:	NoneType
...
"""

x = "Hello, World!"  # str
y = 20               # int
z = 20.5             # float
a = 1j               # complex
b = ["apple", "banana", "cherry"]  # list
c = ("apple", "banana", "cherry")  # tuple
d = range(6)        # range
e = {"name": "John", "age": 36}  # dict
f = {"apple", "banana", "cherry"}  # set
g = frozenset({"apple", "banana", "cherry"})  # frozenset
h = True             # bool 
i = b"Hello"        # bytes
j = bytearray(5)    # bytearray
k = memoryview(bytes(5))  # memoryview
l = None            # NoneType

# Setting the Specific Data Type
x = str("Hello World")  # str
y = int(20)             # int
z = float(20.5)         # float
a = complex(1j)         # complex
b = list(("apple", "banana", "cherry"))  # list
c = tuple(("apple", "banana", "cherry"))  # tuple
d = range(6)            # range
e = dict(name="John", age=36)  # dict
f = set(("apple", "banana", "cherry"))  # set
g = frozenset(("apple", "banana", "cherry"))  # frozenset
h = bool(5)             # bool
i = bytes(5)           # bytes
j = bytearray(5)       # bytearray
k = memoryview(bytes(5))  # memoryview
l = None              # NoneType

