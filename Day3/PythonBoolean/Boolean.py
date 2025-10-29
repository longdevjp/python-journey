# Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)
# or
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Hầu hết các giá trị đều đúng
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Một số giá trị là sai
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

