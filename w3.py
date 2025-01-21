#Lists 
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#Negative indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Ranging and splitting lists
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#And vica versa
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Negative indexing 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#Changing valuse inside a list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
#Changing a range of items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #inserting a valuse at a specified index
#Append items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Extend a value 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) 
#Extending with typle type
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#Removing the item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Removing only first occurence
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#Removing via an index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#Or via the del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) 
#clears the list, but it remains still(empty)
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
