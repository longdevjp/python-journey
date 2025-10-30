thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert 
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # Insert orange at index 1

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # Gộp danh sách tropical vào thislist
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)