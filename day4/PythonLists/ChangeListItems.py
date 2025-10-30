dolong = ["Do", "Re", "Mi", "Fa", "So", "La", "Ti", "Do"]
dolong[3] = "Fah"
print(dolong) # Output: ['Do', 'Re', 'Mi', 'Fah', 'So', 'La', 'Ti', 'Do']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # Output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # Output: ['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # Output: ['apple', 'watermelon']

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #