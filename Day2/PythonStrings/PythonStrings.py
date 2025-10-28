# VD
print("Hello")
print('Hello')

# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Looping Through a String
for x in "banana":
    print(x)

# String Length (Dộ dài chuỗi)
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)
# Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
# Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")