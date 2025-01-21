fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits if x != 'apple']
print(new_list)
#List comprehension 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) 
#setting conditions in list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

