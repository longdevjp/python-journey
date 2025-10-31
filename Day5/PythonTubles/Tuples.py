
mytuple = ("apple", "banana", "cherry")
print(mytuple)  # Output: ('apple', 'banana', 'cherry')

# Cho phép trùng lặp
mytuple = ("apple", "banana", "cherry", "apple", "cherry")
print(mytuple)  # Output: ('apple', 'banana', 'cherry', 'apple', 'cherry')

# Độ dài Tuple
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))  # Output: 3

# Tạo Tuple với một mục
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Kiểu dữ liệu
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple1 = ("abc", 34, True, 40, "male")

# kiểu()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# Hàm tạo tuple()
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

