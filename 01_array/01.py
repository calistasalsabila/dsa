from array import array

# unicode
# array('w') -> one element can only contain one character
# list -> one element can contain a string with multiple characters
letters = array('w', ['a', 'b', 'c', 'd'])

print(letters[2])

# append -> add element at the end
letters.append('e')
print('after append: ', letters)

# extend -> add multiple elements
letters.extend(['f', 'g'])
print('after extend: ', letters)

# insert -> ad an element to specific position; (index before, value)
letters.insert(0, 'e')
print('after insert: ', letters)

# remove -> remove an element by value
letters.remove('e')
print('after remove: ', letters)

# pop -> removes an element by index and returns the removed value
pop = letters.pop() # if no index is specified, it removes the last element
print('after pop: ', pop)

# index -> find the position of an element
index = letters.index('a')
print('index of the value a : ', index)

# count -> count occurances of a value
count =  letters.count('a')
print('count the value of a: ', count)

#  reverse -> reverse the order of the array
letters.reverse()
print('after reverse: ', letters)

#  tobytes -> convert the array to bytes
tobytes = letters.tobytes()
print('convert array to bytes: ', tobytes)

# tolist -> convert the array to a list
tolist = letters.tolist()
print('convert array to list: ', tolist)

# fromlist
letters.fromlist(['h', 'i'])
print('after fromlist: ', letters)

# Note:
# Methods that modify the array in place (append, extend, insert, remove, reverse, fromlist)
# return None, so there is no need to assign them to a variable.
# Methods such as pop, index, count, tobytes, and tolist return a value,
# so their results can be assigned to a variable.