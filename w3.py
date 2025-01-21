Initial commit:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#These values are True, almost any number is True

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#But those are False values

x = 200
print(isinstance(x, int)) #Bult-in function that check whether the variable is of int data type
